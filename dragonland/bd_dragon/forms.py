from .models import Visit
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, DateInput, TimeInput, Select

class VisitForm(ModelForm):
    first_name = forms.CharField(label='Ім\'я', max_length=20, widget=forms.TextInput(attrs={'class': 'form-item form-item-all input-field', 'placeholder': 'Ім\'я'}))
    last_name = forms.CharField(label='Прізвище', max_length=20, widget=forms.TextInput(attrs={'class': 'form-item form-item-all input-field', 'placeholder': 'Прізвище'}))
    email = forms.EmailField(label='E-mail', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-item form-item-all input-field', 'placeholder': 'e-mail'}))

    class Meta:
        model = Visit
        fields = ['first_name', 'last_name', 'email', 'date', 'time', 'dragon']

        widgets = {

            "date": DateInput(attrs={
                'class': 'form-item input-field form-item-all',
                'placeholder': 'Дата візиту'
            }),
            "time": TimeInput(attrs={
                'class': 'form-item input-field form-item-all',
                'placeholder': 'Час візиту'
            }),
            "dragon": Select(attrs={
                'class': 'select form-item form-item-all input-field'
            })
        }

    # class Meta:
    #     model = Visit
    #     fields = ['first_name', 'last_name', 'email', 'date', 'time', 'dragon']
    #
    #     widgets = {
    #         "first_name": TextInput(attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Ім\'я'
    #         }),
    #         "last_name": TextInput(attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Прізвище'
    #         }),
    #         "email": EmailInput(attrs={
    #             'class': 'form-control',
    #             'placeholder': 'E-mail'
    #         }),
    #         "date": DateInput(attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Дата візиту'
    #         }),
    #         "time": TimeInput(attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Час візиту'
    #         }),
    #         "dragon": Select(attrs={
    #             'class': 'form-control'
    #         })
    #     }