from django.contrib import admin
from .models import Submit,complaint,policy,farmer,business,requestproduct

admin.site.register(Submit)
admin.site.register(complaint)
admin.site.register(farmer)
admin.site.register(policy)
admin.site.register(business)
admin.site.register(requestproduct)
