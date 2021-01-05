from django import forms

class CODE_companyForm(forms.Form):
    CODE = forms.CharField(label='CODE', max_length=100)
    