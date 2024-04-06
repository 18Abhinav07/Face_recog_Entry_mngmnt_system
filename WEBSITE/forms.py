from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User , Group
from .models import *
from django import forms
import datetime


class AddNIPDetailsForm(forms.ModelForm):
    
    vehicle_no = forms.CharField(
        required = False,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Vehicle_Number", "class": "form-control"}
        ),
        label="",
    )
 
    
    reason = forms.CharField(
        required = True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Reason for the visit/entry", "class": "form-control"}
        ),
        label="",
    )
    
    name = forms.CharField(
        required = False,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Name", "class": "form-control"}
        ),
        label="",
    )
    
    phone = forms.IntegerField(
        required = False, 
        widget=forms.NumberInput(
            attrs={"placeholder": "Phone", "class": "form-control"}
        ),
        label="",
    )
    
    created_at = forms.CharField(
        initial=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  
        disabled=True,
        widget=forms.widgets.DateTimeInput(
            attrs={"placeholder": "Date and Time", "class": "form-control"}
        ),
        label="",
    )   
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_at'].initial = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    
    class Meta:
        model = NON_INSTITUTE_ADMITTED
        exclude=["user"]