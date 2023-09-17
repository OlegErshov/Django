from django import forms
from .models import Device_type,Issue,FeedBack
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device_type
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

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_type', 'price', 'device_type']

        widgets = {
            "issue_type": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название устройства',
            }),
            "price": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название устройства',
            }),
            "device_type": forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'название устройства',
            }),

        }

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['client_name', 'text', 'image', 'mark','time']

        widgets = {
            "client_na,e": forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите ваше имя',
            }),
            "text": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'введите ваш отзыв',
            }),
            "image": forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'здесь можно прикрепить картинку',
            }),
            "mark": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'оцените нас от 1 до 5',
            }),
            "time": forms.TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите дату отправки отзыва',
            }),


        }


