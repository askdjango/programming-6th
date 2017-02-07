from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm


def post_list(request):
    return render(request, 'journal/post_list.html', {
        'post_list': Post.objects.all(),
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'journal/post_detail.html', {
        'post': post,
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            # post = Post.objects.create(**form.cleaned_data)
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'journal/post_form.html', {
        'form': form,
    })

