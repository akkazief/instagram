from django import forms
from instagram.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("image", "description")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3, "placeholder": "Добавьте описание..."}),
        }