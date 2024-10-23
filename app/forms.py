from django import forms 
from .models import Submit,complaint
class Submitform(forms.ModelForm):
    class Meta:
        model = Submit
        fields = ["product","quantity"]
class complaintform(forms.ModelForm):
    class Meta:
        model = complaint
        fields = ["reply"]