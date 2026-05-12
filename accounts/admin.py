from django.contrib import admin
# accounts/admin.py
from django.contrib import admin
from .models import Agent

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'agency', 'role', 'is_active']
    list_filter = ['agency', 'role', 'is_active']
    search_fields = ['user__first_name', 'user__last_name']

# Register your models here.
