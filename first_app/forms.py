from django import forms
from django.forms import fields, widgets
from requests import models
from .models import Career, DoctorUser

class CarrerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['img']


from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import DoctorUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = DoctorUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = DoctorUser
        fields = ('email',)

class docforms(forms.ModelForm):
    class Meta:
        model = DoctorUser
        fields= ('name', 'last_name', 'mobileno', 'speciality', 'gender', 'education_qualification', 'registration_img', 'profile_img', 'experience', 'doc_about', 'email',)