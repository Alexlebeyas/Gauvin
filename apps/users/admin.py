from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
# from rest_framework.authtoken.models import TokenProxy
from django.contrib.auth.models import Group


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('display_name', 'phone', 'password', )}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name', 'office',)}),
        (_('Permissions'),
         {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        (_('Important dates'),
         {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['email',  'is_superuser']
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', )

admin.site.unregister(Group)
# admin.site.unregister(TokenProxy)
