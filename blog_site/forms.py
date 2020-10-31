from django import forms
from django.core.exceptions import ValidationError
from .models import *


def check_slug(object):
    new_slug = object.lower()
    if new_slug == 'create':
        raise ValidationError('Такая ссылка не может быть создана.')
    return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple()
        }

    def clean_slug(self):
        checked_slug = check_slug(self.cleaned_data['slug'])
        return checked_slug


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        checked_slug = check_slug(self.cleaned_data['slug'])
        return checked_slug
