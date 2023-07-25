from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import TokenProxy

from .models import User, Frequency, Contact, Representative, Language, ContactSubType, ContactType


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('phone_1', 'password',)}),
        (_('Personal info'),
         {'fields': ('last_name', 'first_name',)}),
        (_('Permissions'),
         {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['id', 'email', 'is_superuser']
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


@admin.register(Frequency)
class FrequencyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'description_en', 'month']


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'company']


@admin.register(Representative)
class RepresentativeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_admin']


@admin.register(Language)
class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'description_en']


@admin.register(ContactSubType)
class ContactSubTypeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'description_en', 'contact_type_id']


@admin.register(ContactType)
class ContactTypeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'description_en', 'is_system']


admin.site.unregister(Group)
admin.site.unregister(TokenProxy)
