from django import forms
from django.forms import ModelForm

from forums.models import Message

field_class = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"

class MessageForm(ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(attrs={"class": field_class}),
        label="Message...",
        max_length=30,
    )

    class Meta:
        model = Message
        fields = ["content"]
