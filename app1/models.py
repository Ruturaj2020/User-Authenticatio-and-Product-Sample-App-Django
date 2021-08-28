import django
from django.db import models
from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
# Create your models here.

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class postview(models.Model):
    username = models.ForeignKey(User,default=None,on_delete=CASCADE)
    postin = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.username)
    