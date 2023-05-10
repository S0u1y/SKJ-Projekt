from django import forms
from .models import Comment, User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['document']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['permission', 'activeUntil']