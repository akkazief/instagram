from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from accounts.forms import RegisterForm


User = get_user_model()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/registration.html"
    model = User

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        redirect_url = reverse("posts_list")

        if self.request.GET.get("next"):
            redirect_url = self.request.GET.get("next")

        if self.request.POST.get("next"):
            redirect_url = self.request.POST.get("next")
        return redirect_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "form_title": "Регистрация",
                "form_action": self.request.path,
                "form_id": "register-form",
                "btn_txt": "Зарегистрироваться",
                "form_enctype": "multipart/form-data",
            }
        )
        return context
