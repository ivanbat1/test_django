from django.forms import ModelForm, forms
from .models import *



class AddNewBook(forms.Form, ModelForm):
    class Meta():
        model = Product
        exclude = ['']

from django import forms


class Change(forms.Form):
    price = forms.DecimalField(required=True)
    discount = forms.IntegerField(required=True)
    description = forms.CharField(required=True)
    short_description = forms.CharField(required=True)
    is_active = forms.BooleanField(required=True)
    update = forms.DateField(widget=forms.SelectDateWidget())