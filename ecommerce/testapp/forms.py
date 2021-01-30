from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from testapp.models import Confirmation


class ConfirmationForm(forms.ModelForm):
    class Meta:
        model=Confirmation
        fields="__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last Name'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email','type':'email','id':'exampleInputEmail1','aria-describedby':'emailHelp'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city Name'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state Name'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter pincode Number'}),

        }

'''class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1', 'password2']'''
