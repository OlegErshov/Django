from django import forms
from .models import Device
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'image', 'device_category']

        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название устройства',
            }),
            "image": forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'картинка устройства'
            }),
            "device_category":forms.Select(attrs={
                'class': 'form-control'
            })
        }
