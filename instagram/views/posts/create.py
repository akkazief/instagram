from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from instagram.forms import PostForm
from instagram.models import Post


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create_post.html"
    success_url = reverse_lazy("posts_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "form_title": "Новая публикация",
                "form_action": self.request.path,
                "form_id": "post-form",
                "btn_txt": "Опубликовать",
                "form_enctype": "multipart/form-data",
            }
        )
        return context
