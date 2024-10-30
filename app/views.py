from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from.models import Submit,complaint,feedback,policy,farmer,business,requestproduct
from .forms import Submitform,complaintform,policyform,farmerform,businessform,requestproductform

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
            return redirect('viewcomplaintclass')
        
class Businessproducttable(View):
    def get(self,request):
        xyz=Submit.objects.all()
        return render(request,"business/table.html",{'x':xyz})
class businesscomplaintclass(View):
    def get(self,request):
        return render(request,"business/registercomplaint.html")
    def post(self,request):
        hij=complaintform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return render(request,"business/registercomplaint.html")
class registercomplaintclass(View):
    def get(self,request):
        xyz=complaint.objects.all()
        return render(request,"business/registercomplaint.html",{'x':xyz})
class Policyadd(View):
    def get(self,request):
        return render(request,"admin/policy.html")
    def post(self,request):
        hij=policyform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return render(request,"admin/policy.html")
class Policytable(View):
    def get(self,request):
        xyz=policy.objects.all()
        return render(request,"admin/policytable.html",{'x':xyz})
    
class Policyedit(View):
    #edit clicked
    def get(self,request,pol):
        xyz=policy.objects.filter(id=pol).first()
        return render(request,'admin/policyedit.html',{'x':xyz})
    #update form
    def post(self,request,pol):
        xyz=policy.objects.filter(id=pol).first()
        hij=policyform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=policy.objects.all()
            return render(request,"admin/policytable.html",{'x':abc})
    
class Policydelete(View):
    #edit clicked
    def get(self,request,pol):
        xyz=policy.objects.filter(id=pol).first()
        return render(request,'admin/policydelete.html',{'x':xyz})
    #update form
    def post(self,request,pol):
        xyz=policy.objects.filter(id=pol).first()
        xyz.delete()
        abc=policy.objects.all()
        return render(request,"admin/policytable.html",{'x':abc})
class Farmertable(View):
    def get(self,request):
        xyz=farmer.objects.all()
        return render(request,"admin/farmertable.html",{'x':xyz})
    
class Farmeredit(View):
    #edit clicked
    def get(self,request,far):
        xyz=farmer.objects.filter(id=far).first()
        return render(request,'admin/farmeredit.html',{'x':xyz})
    #update form
    def post(self,request,far):
        xyz=farmer.objects.filter(id=far).first()
        hij=farmerform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=farmer.objects.all()
            return render(request,"admin/farmertable.html",{'x':abc})
    
class Farmerdelete(View):
    #edit clicked
    def get(self,request,far):
        xyz=farmer.objects.filter(id=far).first()
        return render(request,'admin/farmerdelete.html',{'x':xyz})
    #update form
    def post(self,request,far):
        xyz=farmer.objects.filter(id=far).first()
        xyz.delete()
        abc=farmer.objects.all()
        return render(request,"admin/farmertable.html",{'x':abc})
    
class Businessadd(View):
    def get(self,request):
        return render(request,"business/business.html")
    def post(self,request):
        hij=businessform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return render(request,"business/business.html")
        
class Businessregtable(View):
    def get(self,request):
        xyz=business.objects.all()
        return render(request,"business/businessregtable.html",{'x':xyz})
    
class Businessedit(View):
    #edit clicked
    def get(self,request,bus):
        xyz=business.objects.filter(id=bus).first()
        return render(request,'business/businessregedit.html',{'x':xyz})
    #update form
    def post(self,request,bus):
        xyz=business.objects.filter(id=bus).first()
        hij=businessform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=business.objects.all()
            return render(request,"business/businessregtable.html",{'x':abc})
    
class Businessdelete(View):
    #edit clicked
    def get(self,request,bus):
        xyz=business.objects.filter(id=bus).first()
        return render(request,'business/businessregdelete.html',{'x':xyz})
    #update form
    def post(self,request,bus):
        xyz=business.objects.filter(id=bus).first()
        xyz.delete()
        abc=business.objects.all()
        return render(request,"business/businessregtable.html",{'x':abc})
    
class Requestproductadd(View):
    def get(self,request):
        return render(request,"business/requestproduct.html")
    def post(self,request):
        hij=requestproductform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return render(request,"business/requestproduct.html")
        

class Requestproducttable(View):
    def get(self,request):
        xyz=requestproduct.objects.all()
        return render(request,"business/requestproducttable.html",{'x':xyz})
    
class Requestproductedit(View):
    #edit clicked
    def get(self,request,req):
        xyz=requestproduct.objects.filter(id=req).first()
        return render(request,'business/requestproductedit.html',{'x':xyz})
    #update form
    def post(self,request,req):
        xyz=requestproduct.objects.filter(id=req).first()
        hij=requestproductform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=requestproduct.objects.all()
            return render(request,"business/requestproducttable.html",{'x':abc})
        
class Requestproductdelete(View):
    #edit clicked
    def get(self,request,req):
        xyz=requestproduct.objects.filter(id=req).first()
        return render(request,'business/requestproductdelete.html',{'x':xyz})
    #update form
    def post(self,request,req):
        xyz=requestproduct.objects.filter(id=req).first()
        xyz.delete()
        abc=requestproduct.objects.all()
        return render(request,"business/requestproducttable.html",{'x':abc})