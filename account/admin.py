from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class UserModelAdmin(UserAdmin):
    model = User
    list_display = ('email', 'full_name', 'is_active', 'is_staff', 'is_superuser', 'created_at')
    list_filter = ('is_superuser', 'is_active', 'is_staff')
    fieldsets = (
        ('Personal Details', {'fields': ('full_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('full_name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


# Register your models here.
admin.site.register(User, UserModelAdmin)