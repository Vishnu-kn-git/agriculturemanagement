from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from.models import Submit,complaint,feedback
from .forms import Submitform,complaintform

class Submitadd(View):
    def get(self,request):
        return render(request,"admin/submit.html")
    def post(self,request):
        hij=Submitform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return render(request,"admin/submit.html")
class Table(View):
    def get(self,request):
        xyz=Submit.objects.all()
        return render(request,"admin/table.html",{'x':xyz})
class Tabledit(View):
    #edit clicked
    def get(self,request,vijila):
        xyz=Submit.objects.filter(id=vijila).first()
        return render(request,'admin/tableedit.html',{'x':xyz})
    #update form
    def post(self,request,vijila):
        xyz=Submit.objects.filter(id=vijila).first()
        hij=Submitform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=Submit.objects.all()
            return render(request,"admin/table.html",{'x':abc})
    
class Tabledelete(View):
    #edit clicked
    def get(self,request,vijila):
        xyz=Submit.objects.filter(id=vijila).first()
        return render(request,'admin/tabledelete.html',{'x':xyz})
    #update form
    def post(self,request,vijila):
        xyz=Submit.objects.filter(id=vijila).first()
        xyz.delete()
        abc=Submit.objects.all()
        return render(request,"admin/table.html",{'x':abc})
class feedbackclass(View):
    def get(self,request):
        xyz=feedback.objects.all()
        return render(request,"admin/feedback.html",{'x':xyz})
class complaintclass(View):
    def get(self,request):
        xyz=complaint.objects.all()
        return render(request,"admin/complaint.html",{'x':xyz})

class complaintedit(View):
    #edit clicked
    def get(self,request,comp):
        xyz=complaint.objects.filter(id=comp).first()
        return render(request,'admin/complaintedit.html',{'x':xyz})
    #update form
    def post(self,request,comp):
        xyz=complaint.objects.filter(id=comp).first()
        hij=complaintform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            return redirect('admin/complaintclass')
        
class Businesstable(View):
    def get(self,request):
        xyz=Submit.objects.all()
        return render(request,"business/table.html",{'x':xyz})
class businesscomplaintclass(View):
    def get(self,request):
        xyz=complaint.objects.all()
        return render(request,"business/complaint.html",{'x':xyz})
class registercomplaintclass(View):
    def get(self,request):
        xyz=complaint.objects.all()
        return render(request,"register_complaint.html",{'x':xyz})