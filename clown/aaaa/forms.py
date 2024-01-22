from django import forms
from django.shortcuts import render
class InputForm(forms.Form):
    Name = forms.CharField(max_length=200)
    LastName = forms.CharField(max_length=200)
