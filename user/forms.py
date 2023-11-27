from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from typing import Any
from django import forms

class Userform(UserCreationForm):
    email = forms.EmailField(max_length=75, required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_text = {
            'username': None,
        }
        

    def __init__(self, *args: Any, **kwargs):
        super(Userform, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
      

# class ProfileUpdate(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image',]