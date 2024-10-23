from django.urls import path
from .views import Submitadd,Table,Tabledelete,Tabledit,feedbackclass,complaintclass,complaintedit,Businesstable,businesscomplaintclass,registercomplaintclass

urlpatterns = [
    path('submitapp/',Submitadd.as_view()),
    path('table/',Table.as_view()),
    path('tableedit/<vijila>',Tabledit.as_view()),
    path('tabledelete/<vijila>',Tabledelete.as_view()),
    path('feedbackclass/',feedbackclass.as_view()),
    path('complaintclass/',complaintclass.as_view(),name='complaintclass'),
    path('complaintedit/<comp>',complaintedit.as_view()),
    path('businesstable/',Businesstable.as_view()),
    path('businesscomplaintclass/',businesscomplaintclass.as_view(),name='complaintclass'),
    path('registercomplaintclass/',registercomplaintclass.as_view(),name='complaintclass')

]