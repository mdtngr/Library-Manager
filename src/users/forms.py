from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from users.models import UserData,Userprofile



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length= 60, help_text = 'Required. Add a valid email')

    class Meta:
        model       =  UserData
        fields      =  ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'year_of_joining', 'roll_no')

class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label ='Password', widget = forms.PasswordInput)

    class Meta:
        model = UserData
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email = email, password = password):
                raise forms.ValidationError("Invalid Login")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['username','phone_number','email','address','profile_picture']

        