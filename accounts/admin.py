# accounts/admin.py
from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Doctor, DoctorApplication

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, UserAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty')
    search_fields = ('user__email', 'specialty')
    
    def save_model(self, request, obj, form, change):
        obj.user.is_doctor = True  # Ensure the is_doctor field is set to True
        obj.user.save()
        super().save_model(request, obj, form, change)

admin.site.register(Doctor, DoctorAdmin)     

class DoctorApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'specialty', 'applied_at')
    search_fields = ('user__email', 'status', 'specialty')

    def save_model(self, request, obj, form, change):
        if obj.status == 'Approved' and obj.user.is_doctor == False:
            obj.user.is_doctor = True
            obj.user.save()
            # Create a Doctor instance if it does not exist
            if not Doctor.objects.filter(user=obj.user).exists():
                Doctor.objects.create(
                    user=obj.user,
                    specialty=obj.specialty,
                    certificate=obj.certificate
                )
        super().save_model(request, obj, form, change)

admin.site.register(DoctorApplication, DoctorApplicationAdmin)