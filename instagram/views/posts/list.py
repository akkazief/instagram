# instagram/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from instagram.models import Post


class ListPostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        return (
            Post.objects
            .select_related("author")
            .order_by("-created_at")
        )