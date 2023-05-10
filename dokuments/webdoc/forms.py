from django import forms
from .models import Comment, User, Payment, Address


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['document']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['permission', 'activeUntil']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['date']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name']
