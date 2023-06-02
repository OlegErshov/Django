from django.contrib import admin
from .models import Device,Issue,Category
# Register your models here.


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'device_category']

@admin.register(Category)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Issue)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['issue_type', 'device_type', 'price']
