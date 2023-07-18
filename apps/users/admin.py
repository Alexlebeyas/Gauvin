from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Tblcontactsecondaire as User, Tblfrequence, Tblcontact, Tblrepresentant, Tbllangue, Tbltypecontactsous, Tbltypecontact
from rest_framework.authtoken.models import TokenProxy
from django.contrib.auth.models import Group


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('ctelephone1', 'password', )}),
        (_('Personal info'),
         {'fields': ('cprenom', 'cnom',)}),
        (_('Permissions'),
         {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        (_('Important dates'),
         {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('cemail', 'password1', 'password2'),
        }),
    )
    list_display = ['icligne', 'cemail',  'is_superuser']
    search_fields = ('cemail', 'cprenom', 'cnom')
    ordering = ('cemail', )


@admin.register(Tblfrequence)
class TblfrequenceModelAdmin(admin.ModelAdmin):
    list_display = ['icfrequence', 'cdescription', 'cdescriptionan', 'nmois']


@admin.register(Tblcontact)
class TblcontactModelAdmin(admin.ModelAdmin):
    list_display = ['iccontact', 'centreprise', 'csalutation', 'cnom']


@admin.register(Tblrepresentant)
class TblrepresentantModelAdmin(admin.ModelAdmin):
    list_display = ['icrepresentant', 'cnom', 'ladmin', 'cmotpasse']


@admin.register(Tbllangue)
class TbllangueModelAdmin(admin.ModelAdmin):
    list_display = ['iclangue', 'cdescription', 'cdescriptionan']


@admin.register(Tbltypecontactsous)
class TbltypecontactsousModelAdmin(admin.ModelAdmin):
    list_display = ['ictype', 'cdescription', 'cdescriptionan', 'ntype']


@admin.register(Tbltypecontact)
class TbltypecontactModelAdmin(admin.ModelAdmin):
    list_display = ['ictype', 'cdescription', 'cdescriptionan', 'lsysteme', 'ssma_timestamp']


admin.site.unregister(Group)
admin.site.unregister(TokenProxy)
