from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


class AccountChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Account
        

class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    list_display = ('username', 'tier', 'is_staff')

    fieldsets = (
            (None, {'fields': ('username', 'email', 'password', 'tier', 'is_staff')}),
        )   


admin.site.register(Account, AccountAdmin)
