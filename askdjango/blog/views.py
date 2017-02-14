from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm


def post_list(request):
    return render(request, 'blog/post_list.html', {
        'post_list': Post.objects.all(),
    })


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
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
    post = Post.objects.get(pk=pk)

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


@login_required
def comment_new(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # form.cleaned_data
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, '새 댓글을 저장했습니다.')
            return redirect(comment.post)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form': form,
    })


@login_required
def comment_edit(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)
    if comment.user != request.user:
        messages.warning(request, '댓글 작성자만 수정할 수 있습니다.')
        return redirect(comment.post)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            messages.success(request, '기존 댓글을 수정했습니다.')
            return redirect(comment.post)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {
        'form': form,
    })


@login_required
def comment_delete(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)
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

