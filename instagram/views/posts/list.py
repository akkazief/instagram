from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from instagram.models import Post


class ListPostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        following_ids = self.request.user.following.values_list("following_id", flat=True)
        return (
            Post.objects
            .filter(author_id__in=following_ids)
            .select_related("author")
            .order_by("-created_at")
        )