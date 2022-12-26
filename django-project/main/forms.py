from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "rows": 3,
                "placeholder": "What's on your mind?",
                "class": "textarea is-success is-medium form-control form-control form-status border-0 py-1 px-0",
            }
        ),
        label="",
    )

    class Meta:
        model = Post
        exclude = ("username", )


