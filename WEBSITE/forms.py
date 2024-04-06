from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User , Group
from django import forms

class AddStudentDetailsForm(forms.ModelForm):
    
    vehicle_number = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Vehicle_Number", "class": "form-control"}
        ),
        label="",
    )
    
    reason = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Cause for late entry", "class": "form-control"}
        ),
        label="",
    )
    
    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "City", "class": "form-control"}
        ),
        label="",
    )


    class Meta:
        model = Student_detail
        exclude = ("user",)