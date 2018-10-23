from django import forms
from .models import Users, fcm_info, verify_user


class UserForm(forms.ModelForm):
    class Meta:
        model=verify_user
        fields=('phone_no','password')