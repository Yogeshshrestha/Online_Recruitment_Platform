from tkinter import Widget
from django import forms
from .models import Profile, Skill


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'country', 'location',
                  'resume', 'grad_year', 'looking_for']
        widgets = {'full_name': forms.TextInput(
            attrs={'class': 'input__profile'}),
            # 'country': forms.widgets.NullBooleanSelect(attrs={'class': 'input__profile input-choice'}),
            'location': forms.TextInput(attrs={'class': 'input__profile'}),
            'resume': forms.FileInput(attrs={'class': 'input__profile-fie'}),
            'grad_year': forms.TextInput(attrs={'class': 'input__profile'}),
            # 'looking_for': forms.widgets.NullBooleanSelect(attrs={'class': 'input__profile input-choice'})
        }


class NewSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']
