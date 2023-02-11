from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    labelAttr = "block mb-2 text-sm font-medium text-white"
    inputAttr = "border sm:text-sm rounded-lg focus:border-primary-600 block w-full p-2.5 bg-gray-700 text-white focus:ring-blue-500 focus:border-blue-500"
    selectAttr = "border sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block bg-gray-700 w-full p-2.5 border-gray-600 text-white focus:ring-blue-500 focus:border-blue-500"

    first_name = forms.CharField(required=True, label="Prénom")
    last_name = forms.CharField(required=True, label="Nom")
    email = forms.EmailField(required=True, label="Email")
    password1 = forms.CharField(
        required=True, label="Mot de passe", widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        required=True, label="Confirmation", widget=forms.PasswordInput
    )
    username = forms.CharField(required=True, label="Nom d'utilisateur")
    role = forms.ChoiceField(
        choices=[("READER", "Lecteur"), ("LIBRARIAN", "Libraire")],
        label="Vous êtes ?",
    )

    first_name.widget.attrs.update({"class": inputAttr})
    last_name.widget.attrs.update({"class": inputAttr})
    email.widget.attrs.update({"class": inputAttr})
    password1.widget.attrs.update({"class": inputAttr})
    password2.widget.attrs.update({"class": inputAttr})
    username.widget.attrs.update({"class": inputAttr})
    role.widget.attrs.update({"class": selectAttr})

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
        )
