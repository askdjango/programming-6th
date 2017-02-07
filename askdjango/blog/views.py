from django.shortcuts import render
from blog.models import Post


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
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    return render(request, 'blog/post_form.html')

