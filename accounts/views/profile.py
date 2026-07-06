from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from instagram.models import Follow

User = get_user_model()


def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = profile_user.posts.select_related("author").all()

    is_following = False
    if request.user.is_authenticated and request.user != profile_user:
        is_following = Follow.objects.filter(
            follower=request.user, following=profile_user
        ).exists()

    context = {
        "profile_user": profile_user,
        "posts": posts,
        "is_following": is_following,
    }
    return render(request, "profile/profile.html", context)
