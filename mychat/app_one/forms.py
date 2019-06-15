from django import forms
from app_one.models import Post,Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta():
        model=Post
        fields=['message','title']


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
