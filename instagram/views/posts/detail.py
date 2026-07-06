from django.views.generic import DetailView

from instagram.forms import CommentForm
from instagram.models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context["is_liked"] = (
            user.is_authenticated and self.object.likes.filter(user=user).exists()
        )
        context["likes_count"] = self.object.likes.count()
        context["comments"] = self.object.comments.select_related("author")
        context["comment_form"] = CommentForm()
        return context
