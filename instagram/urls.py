from django.urls import path
from instagram.views import CreatePostView, ListPostView


urlpatterns = [
    path("posts/create/", CreatePostView.as_view(), name="create_post"),
    path("", ListPostView.as_view(), name="posts_list"),
]