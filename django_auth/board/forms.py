# coding: utf-8
from django import forms
from django.contrib.auth.models import User

from board.models import Board


class AddMessageForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('content', )

    #def save():
