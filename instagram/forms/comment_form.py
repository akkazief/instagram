from django import forms

from instagram.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.TextInput(attrs={"placeholder": "Добавьте комментарий..."})
        }
        labels = {"text": ""}