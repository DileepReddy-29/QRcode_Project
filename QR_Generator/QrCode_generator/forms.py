from django import forms

class QRCodeForm(forms.Form):
    Company_name = forms.CharField(
        label='Company Name',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder': 'Company Name'
            
            })
        )
    url = forms.URLField(
        label='URL',
        max_length=255,
        widget=forms.URLInput(attrs={
            'class' : 'form-control',
            'placeholder': 'Enter URL'
        })
        )