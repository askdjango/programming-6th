from django.shortcuts import redirect, render
from blog.models import Post
from blog.forms import PostForm


def post_list(request):
    return render(request, 'blog/post_list.html', {
        'post_list': Post.objects.all(),
    })


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def post_new(request):
    if request.method == 'GET':
        form = PostForm()
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print('통과한 값 : ', form.cleaned_data)
            # return redirect(post)
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog:post_list')
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'GET':
        form = PostForm(instance=post)
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            print('통과한 값 : ', form.cleaned_data)
            # return redirect(post)
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog:post_list')
    return render(request, 'blog/post_form.html', {
        'form': form,
    })

