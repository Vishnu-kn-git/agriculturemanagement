from django import forms 
from .models import Submit,complaint,policy,farmer,business
class Submitform(forms.ModelForm):
    class Meta:
            model = Submit
            fields = ["product","quantity"]
class complaintform(forms.ModelForm):
    class Meta:
        model = complaint
        fields = ["userid","description","reply"]
class policyform(forms.ModelForm):
    class Meta:
        model = policy
        fields = ["policyname","date","description"]
class farmerform(forms.ModelForm):
    class Meta:
        model = farmer
        fields = ["farmername","email","contactnumber"]

class businessform(forms.ModelForm):
    class Meta:
        model = business
        fields = ["name","companyname","email","number","password"]