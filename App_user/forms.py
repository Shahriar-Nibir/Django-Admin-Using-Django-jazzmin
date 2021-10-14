# from django.forms import ModelForm, model_to_dict, fields_for_model
from django import forms
from django.contrib.auth.models import User
from .models import *


class AppUserForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['account', 'username', 'password', 'confirm_password', 'email',
                  'groups', 'first_name', 'last_name', 'contact_no', 'profile_pic', 'active']
        # exclude = ['user']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    # def save(self, commit=True):
        # temp = super(AppUserForm, self).save(commit=False)
    #     # user.set_username(self.cleaned_data["username"])
    #     # user.set_password(self.cleaned_data["password1"])
    #     username = self.cleaned_data['username']
    #     account = self.cleaned_data['username']
    #     print('hi '+username)
    #     password1 = self.cleaned_data['password1']
    #     print(password1)
    #     password2 = self.cleaned_data['password2']
    #     email = self.cleaned_data['email']
    #     groups = self.cleaned_data['groups']
    #     first_name = self.cleaned_data['first_name']
    #     last_name = self.cleaned_data['last_name']
    #     active = self.cleaned_data['active']
    #     user = User.objects.create(username=username, password=password1, email=email,
    #                                is_active=active)
    #     user.save()
    #     # temp.user = user

    #     t, created = AppUser.objects.update_or_create(
    #         user=user, email=email)
    #     groups.appUser_set.add(groups)
    #     # t.username = username
    #     # t.profile_pic = profile_pic
    #     # t.save(commit=False)
    #     t.save()

    #     # temp.save()
    #     return user
