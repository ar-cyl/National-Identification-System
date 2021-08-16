from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.modelfields import PhoneNumberField

from accounts.models import MyPersonalDetail, Approval

class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField(required=False)

    # gives nested namespace for configuration and interacts with User model
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
class MyProfileForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    phone = PhoneNumberField()

    class Meta:
        model = MyPersonalDetail
        fields = ['email','phone']


class ApprovalForm(forms.ModelForm):
       class Meta:
        model = Approval
        fields = ['approved_document']