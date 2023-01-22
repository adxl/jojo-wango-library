from django import forms
from django.forms import ModelForm

from libraries.models import Library

field_class = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"


class NameForm(ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': field_class

            }
        ),
        label="Library name",
        max_length=120
    )

    latitude = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class': field_class
            }
        ),
        label="Latitude",
    )

    longitude = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class': field_class
            }
        ),
        label="Longitude",
    )

    class Meta:
        model = Library
        fields = ['name', 'latitude', 'longitude']
