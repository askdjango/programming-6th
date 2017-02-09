from django.views.generic import CreateView, UpdateView
from blog.models import Post
from blog.forms import PostForm


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        return super().form_valid(form)

post_new = PostCreateView.as_view()

post_edit = UpdateView.as_view(model=Post, form_class=PostForm)

