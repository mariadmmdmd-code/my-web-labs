from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    list_filter = ('is_staff', 'is_active')
    
    # Поля, которые показывать при редактировании
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('bio',)}),
    )

admin.site.register(User, CustomUserAdmin)