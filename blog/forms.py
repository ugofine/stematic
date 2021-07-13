from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "name"
        })
    )
    body = forms.CharField(max_length=250, widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "comment"
        })
    )
    email = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "email"
        })

    )

