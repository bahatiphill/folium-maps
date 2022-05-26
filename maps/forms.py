from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Coordinates


class CoordinatesForm(forms.ModelForm):

    #lat = forms.CharField(max_length=20)
    #lon = forms.CharField(max_length=20)

    class Meta:
        model = Coordinates
        fields = '__all__'