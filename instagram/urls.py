from django.urls import path
from instagram.views import CreatePostView, ListPostView, FollowView, PostDetailView, LikeView



urlpatterns = [
    path("posts/create/", CreatePostView.as_view(), name="create_post"),
    path("", ListPostView.as_view(), name="posts_list"),
    path("<str:username>/follow/", FollowView.as_view(), name="follow"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/like/", LikeView.as_view(), name="like"),
]