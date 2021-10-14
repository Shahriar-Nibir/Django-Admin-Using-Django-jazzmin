from django import forms
from django.contrib.auth.models import User
from .models import *


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['account', 'username', 'password', 'confirm_password', 'email',
                  'first_name', 'last_name', 'contact_no', 'active']
        # exclude = ['user']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['account'].queryset = User.objects.filter(
                is_staff=True, is_superuser=True)
