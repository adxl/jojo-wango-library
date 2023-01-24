from django import forms
from django.forms import ModelForm

from libraries.models import Library
from reading_groups.models import ReadingGroup

field_class = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"


class ReadingGroupForm(ModelForm):
    start_at = forms.DateTimeField(
        widget=forms.TextInput(attrs={"class": field_class, "type": "datetime-local"}),
        label="Reading group start time",
    )

    end_at = forms.DateTimeField(
        widget=forms.TextInput(attrs={"class": field_class, "type": "datetime-local"}),
        label="Reading group end time",
    )

    library = forms.ModelChoiceField(
        queryset=Library.objects.all(),
        to_field_name="name",
        label="Bibliothèque",
    )

    class Meta:
        model = ReadingGroup
        fields = ["start_at", "end_at", "library"]
