from django import forms
from .models import Agent


class AgentForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name: ")
    phone = forms.IntegerField(help_text="Phone Number: ")
    username = forms.CharField(help_text="Username", max_length=20)
    email = forms.CharField(help_text="Email", max_length=50)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput, help_text="Password")
    address = forms.CharField(max_length=128, help_text="Address: ", required=False)
    photo = forms.ImageField(help_text="Upload image/logo: ")
    description = forms.CharField(max_length=500, help_text="Description: ", required=False)

    class Meta:
        model = Agent
        fields = ('name', 'phone', 'username', 'email', 'address', 'photo', 'description')
