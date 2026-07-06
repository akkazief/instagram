from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render

User = get_user_model()

def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = profile_user.posts.select_related("author").all()
    context = {
        "profile_user": profile_user,
        "posts": posts,
    }
    return render(request, "profile/profile.html", context)