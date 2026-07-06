# accounts/views.py
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.views.generic import ListView
from accounts.forms import UserSearchForm

User = get_user_model()


class UserSearchView(ListView):
    model = User
    template_name = "accounts/search.html"
    context_object_name = "users"
    paginate_by = 10

    def get_query(self):
        return self.request.GET.get("q", "").strip()

    def get_queryset(self):
        query = self.get_query()
        if not query:
            return User.objects.none()
        return User.objects.filter(
            Q(username__icontains=query)
            | Q(email__icontains=query)
            | Q(first_name__icontains=query)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UserSearchForm(self.request.GET)
        context["query"] = self.get_query()
        return context