from django import forms
from User_App.models import Information

class UserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput)

    class Meta():
        model = Information
        fields = ('email', 'password')