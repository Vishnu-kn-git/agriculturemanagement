from django import forms 
from .models import *
class feedbackform(forms.ModelForm):
    class Meta:
            model = feedback
            fields = ["user","feedback","date","reply"]

class farmerform(forms.ModelForm):
    class Meta:
        model = farmer
        fields = ["user","name","address","place","mobno","kbhavan"]

class productform(forms.ModelForm):
    class Meta:
            model = product
            fields = ["user","date","image","price"]

class requestproductform(forms.ModelForm):
    class Meta:
        model = requestproduct
        fields = ["user","date","quantity","product"]

class complaintform(forms.ModelForm):
    class Meta:
        model = complaint
        fields = ["complaint","reply","date","user"]

class policyform(forms.ModelForm):
    class Meta:
        model = policy
        fields = ["policy","date","category","details","file"]


class businessform(forms.ModelForm):
    class Meta:
        model = business
        fields = ["user","name","address","email","place","mobno"]

class labourform(forms.ModelForm):
    class Meta:
        model = labour
        fields = ["policy","date","status","task"]

class cartform(forms.ModelForm):
    class Meta:
        model = cart
        fields = ["product","date"]

class payform(forms.ModelForm):
    class Meta:
        model = pay
        fields = ["cart","status","product"]

