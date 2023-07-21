from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)

    # form for change information
    fieldsets = (
        ('Authentication', {
            "fields": (
                'email', 'password'
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_active', 'is_staff', 'is_superuser'
            ),
        }),
        ('group permissions', {
            "fields": (
                'groups', 'user_permissions',
            ),
        }),
        ('important date', {
            "fields": (
                'last_login',
            ),
        }),
    )

    # form for add information
    add_fieldsets = (
        ('Authentication', {
            "fields": (
                'email', 'password1', 'password2' 
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_active', 'is_staff', 'is_superuser'
            ),
        })
    )





admin.site.register(User, CustomUserAdmin)


