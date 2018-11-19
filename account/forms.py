from django import forms
from django.core.exceptions import ValidationError

def password_checker(value):
    if len(value) < 8:
        raise ValidationError("Passworld must be more than 8 character")


class UserResgisterForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'forms.control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'forms.control'})
                               ,validators=[password_checker])
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'forms.control'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password != re_password:
            raise forms.ValidationError("password doesn't match")

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'forms.control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'forms.control'}))
