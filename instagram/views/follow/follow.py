from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from instagram.models import Follow

User = get_user_model()


class FollowView(LoginRequiredMixin, View):
    def post(self, request, username):
        target = get_object_or_404(User, username=username)

        if target != request.user:
            follow, created = Follow.objects.get_or_create(
                follower=request.user, following=target
            )
            if not created:
                follow.delete()

        return redirect("accounts:profile", username=username)
