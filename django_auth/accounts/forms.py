# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate


class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'input-block-level'
            field.widget.attrs['placeholder'] = field.label


class LoginForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "email"
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'input-block-level'
            field.widget.attrs['placeholder'] = field.label

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            raise forms.ValidationError("error")

        if user and password:
            self.user_cache = authenticate(username=user.username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError("error")
            elif not self.user_cache.is_active:
                raise forms.ValidationError('error')
        self.check_for_test_cookie()
        return self.cleaned_data

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError("error")

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'input-block-level'
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        model = User
        fields = ('email', 'username', )

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('email必填项')
        return email
