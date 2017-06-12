from django import forms
from weatherApp.admin import UserCreationForm
from weatherApp.models import MyUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2', )