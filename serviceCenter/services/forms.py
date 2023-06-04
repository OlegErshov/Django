from django import forms
from .models import Device
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'image']

        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название устройства',
            }),
            "image": forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'картинка устройства'
            }),

        }
