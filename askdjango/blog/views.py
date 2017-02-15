from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm


def post_list(request):
    return render(request, 'blog/post_list.html', {
        'post_list': Post.objects.all(),
    })


def post_detail(request, pk):
#   try:
#       post = Post.objects.get(pk=pk)  # Post.DoesNotExist, Post.MultipleObjectsReturned
#   except (Post.DoesNotExist, Post.MultipleObjectsReturned):
#       raise Http404   # django.http.Http404

    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comment_form': comment_form,
    })


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print('통과한 값 : ', form.cleaned_data)
            # return redirect(post)
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.info(request, '포스팅을 잘 저장했습니다.')
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            print('통과한 값 : ', form.cleaned_data)
            # return redirect(post)
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.info(request, '포스팅을 잘 저장했습니다.')
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def comment_list(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    return render(request, 'blog/_comment_list.html', {
        'comment_list': post.comment_set.all(),
    })


@login_required
def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # form.cleaned_data
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            if request.is_ajax():
                return render(request, 'blog/_comment.html', {
                    'comment': comment,
                })
            messages.success(request, '새 댓글을 저장했습니다.')
            return redirect(comment.post)
    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', {
        'form': form,
    })


@login_required
def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.user != request.user:
        messages.warning(request, '댓글 작성자만 수정할 수 있습니다.')
        return redirect(comment.post)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            if request.is_ajax():
                return render(request, 'blog/_comment.html', {
                    'comment': comment,
                })
            messages.success(request, '기존 댓글을 수정했습니다.')
            return redirect(comment.post)
    else:
        form = CommentForm(instance=comment)

    if request.is_ajax():
        template_name = '_modal_form.html'
    else:
        template_name = 'blog/comment_form.html'

    return render(request, template_name, {
        'form': form,
    })


@login_required
def comment_delete(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.user != request.user:
        messages.warning(request, '댓글 작성자만 삭제할 수 있습니다.')
        return redirect(comment.post)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, '댓글을 삭제했습니다.')
        return redirect(comment.post)
    return render(request, 'blog/comment_confirm_delete.html', {
        'comment': comment,
    })

