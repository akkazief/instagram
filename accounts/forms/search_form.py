from django import forms


class UserSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Поиск по логину, email или имени"}
        ),
    )
