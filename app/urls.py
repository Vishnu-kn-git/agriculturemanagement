from django.urls import path
from .views import Adminhome, Login, Productadd,Table,Tabledelete,Tabledit,feedbackclass,complaintclass,complaintedit,Businessproducttable,businesscomplaintclass,Policyadd,Policytable
from .views import Policyedit,Policydelete,Farmertable,Farmerdelete,Farmeredit,Businessadd,Businessregtable
from .views import Businessedit,Businessdelete,Requestproductadd,Requestproducttable,Requestproductedit,Requestproductdelete
urlpatterns = [
    path('submitapp/',Productadd.as_view()),
    path('table/',Table.as_view()),
    path('tableedit/<vijila>',Tabledit.as_view()),
    path('tabledelete/<vijila>',Tabledelete.as_view()),
    path('feedbackclass/',feedbackclass.as_view()),
    path('complaintclass/',complaintclass.as_view(),name='viewcomplaintclass'),
    path('complaintedit/<comp>',complaintedit.as_view()),
    path('businessproducttable/',Businessproducttable.as_view()),
    path('businesscomplaintclass/',businesscomplaintclass.as_view(),name='complaintclass'),
    path('policy/',Policyadd.as_view()),
    path('policytable/',Policytable.as_view()),
    path('policyedit/<pol>',Policyedit.as_view()),
    path('policydelete/<pol>',Policydelete.as_view()),
    path('farmertable/',Farmertable.as_view()),
    path('farmeredit/<far>',Farmeredit.as_view()),
    path('farmerdelete/<far>',Farmerdelete.as_view()), 
    path('businessapp/',Businessadd.as_view()),
    path('businessregtable/',Businessregtable.as_view()),
    path('businessregedit/<bus>',Businessedit.as_view()),
    path('businessregdelete/<bus>',Businessdelete.as_view()),
    path('requestproductapp/',Requestproductadd.as_view()),
    path('requestproducttable/',Requestproducttable.as_view()),
    path('requestproductedit/<req>',Requestproductedit.as_view()),
    path('requestproductdelete/<req>',Requestproductdelete.as_view()),
    path('adminhome/',Adminhome.as_view(),name='Adminhome'),
    path('',Login.as_view())

]