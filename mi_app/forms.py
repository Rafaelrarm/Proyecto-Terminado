from django import forms
from mi_app.models import User
from django.contrib.auth.forms import UserCreationForm


class CursoFormulario(forms.Form):

    User= forms.CharField(required=True)
    Clave= forms.IntegerField()


class CursoBusquedaFormulario(forms.Form):

    criterio = forms.CharField()

class UserRegisterform(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label='repetir la contraseña', widget= forms.PasswordInput)

    last_name= forms.CharField()
    first_name= forms.CharField()

class meta:
    model = User
    fields = ['username','email','password1','password2','past_name','first_name']
    help_texts = {k:"" for k in fields}
