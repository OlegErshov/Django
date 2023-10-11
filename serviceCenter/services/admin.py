from django.contrib import admin
from .models import Device_type,Issue,News,Stuff,FeedBack
# Register your models here.


@admin.register(Device_type)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

@admin.register(Issue)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['issue_type', 'device_type', 'price']

@admin.register(News)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'description', 'full_text','resource']

@admin.register(Stuff)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'email','phone_number', 'image', 'job_description']

@admin.register(FeedBack)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['client', 'text', 'mark','image', 'time']

