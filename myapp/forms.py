from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class Regis(UserCreationForm):
    email = forms.EmailField(required=True)
    bdate = forms.DateField()

    class Meta:
        model = User
        fields = ["username","email","bdate","password1","password2"]


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","text"]

