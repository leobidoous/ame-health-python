# coding=utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from pessoa.models import User
from pessoa.forms import UserAdminCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):

    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('name', 'email', 'username', 'password1', 'password2', 'type')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'type')
        }),
        ('Informações Básicas', {
            'fields': ('name', 'last_login')
        }),
        (
            'Permissões', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups',
                    'user_permissions'
                )
            }
        ),
    )
    list_display = ['username', 'name', 'email', 'is_active', 'is_staff', 'date_joined', 'type']


admin.site.register(User, UserAdmin)
