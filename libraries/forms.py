from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='library name', max_length=120)