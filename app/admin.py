from django.contrib import admin
from .models import cart, labour, pay, product,complaint,policy,farmer,business,requestproduct,feedback
from django.contrib.auth.forms import UserChangeForm ,UserCreationForm
from django.contrib.auth.admin import UserAdmin
from app.models import LoginTable
admin.site.register(product)
admin.site.register(complaint)
admin.site.register(farmer)
admin.site.register(policy)
admin.site.register(business)
admin.site.register(requestproduct)
admin.site.register(labour)
admin.site.register(cart)
admin.site.register(pay)
admin.site.register(feedback)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = LoginTable
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = LoginTable
        exclude = []



class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (('this is heading'), {"fields": ("username", "password")}),
        (
            ("Personal info"),
            {
                "fields": (
                    "email",
                    "first_name",
                )
            },
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "user_type",
                    "is_active",
                    "is_superuser",
                    "status"
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("username", "password1", "password2")},
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ("pk","username", "first_name", "user_type")
    search_fields = ("username", "first_name")
    ordering=("username",)


admin.site.register(LoginTable,CustomUserAdmin)