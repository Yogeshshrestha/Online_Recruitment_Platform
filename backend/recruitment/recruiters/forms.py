from django import forms
from .models import Job


class NewJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location',
                  'description', 'skills_req', 'job_type', 'link']
        help_texts = {
            'skills_req': 'Enter all the skills required each separated by commas.',
        }
        widgets = {'title': forms.TextInput(
            attrs={'class': 'input__job'}),
            'company':  forms.TextInput(attrs={'class': 'input__job'}),
            'location': forms.TextInput(attrs={'class': 'input__job'}),
            'description': forms.Textarea(attrs={'class': 'input__job input-desc'}),
            'skills_req': forms.TextInput(attrs={'class': 'input__job'}),
            # 'job_type': forms.widgets.NullBooleanSelect(attrs={'class': 'input__job input-choice'}),
            'link': forms.URLInput(attrs={'class': 'input__job'}),
        }


class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location',
                  'description', 'skills_req', 'job_type', 'link']
        help_texts = {
            'skills_req': 'Enter all the skills required each separated by commas.',
            'link': 'If you want candidates to apply on your company website rather than on our website, please provide the link where candidates can apply. Otherwise, please leave it blank or candidates would not be able to apply directly!',
        }
        widgets = {'title': forms.TextInput(
            attrs={'class': 'input__job'}),
            'company':  forms.TextInput(attrs={'class': 'input__job'}),
            'location': forms.TextInput(attrs={'class': 'input__job'}),
            'description': forms.Textarea(attrs={'class': 'input__job input-desc'}),
            'skills_req': forms.TextInput(attrs={'class': 'input__job'}),
            # 'job_type': forms.widgets.NullBooleanSelect(attrs={'class': 'input__job input-choice'}),
            'link': forms.URLInput(attrs={'class': 'input__job'}),
        }
