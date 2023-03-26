from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class RegisterUser(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = "__all__"
        exclude = ['user_name']

class CaptchaRegForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)