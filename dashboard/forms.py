from dataclasses import field, fields
from random import choices
from tkinter import Widget
from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description']

class DataInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due':DataInput()}
        fields = ['subject','title','description','due','is_finished']

class DashboardFom(forms.Form):
    text = forms.CharField(max_length=100,label="Enter your Search : ")

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished'] 

class ConversionForm(forms.Form):
    CHOICES = [('length','Length'),('mass','Mass')]
    measurement = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)


class ConversionLengthForm(forms.Form):
    CHOICES = [('yard','Yard'),('foot','Foot')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs= {'type':'number','placeholder':'Enter the number'}
    ))
    measure1= forms.CharField(
        label= "",widget= forms.Select(choices=CHOICES)
    )
    measure2= forms.CharField(
        label= "",widget= forms.Select(choices=CHOICES)
    )


class ConversionMassForm(forms.Form):
    CHOICES = [('pound','Pound'),('kilogram','Kilogram')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs= {'type':'number','placeholder':'Enter the number'}
    ))
    measure1= forms.CharField(
        label= "",widget= forms.Select(choices=CHOICES)
    )
    measure2= forms.CharField(
        label= "",widget= forms.Select(choices=CHOICES)
    )

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2'] 
        