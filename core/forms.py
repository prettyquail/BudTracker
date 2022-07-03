from core.models import Account
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username','email','password']

