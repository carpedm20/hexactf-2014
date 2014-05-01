from django import forms
from django.utils.html import strip_tags

from .models import Problem

class ProblemCreateForm(forms.ModelForm):
    score = forms.ChoiceField(choices=Problem.SCORE_CHOICES, widget=forms.Select())
    context = forms.ChoiceField(choices=Problem.CONTEXT_CHOICES, widget=forms.Select())

    link = forms.URLField()
    file = forms.FileField()

    def is_valid(self):
        form = super(AccountCreateForm, self).is_valid()
        return form

    class Meta:
        model = Problem
        fields = ['score', 'context', 'link', 'file']

    def save(self, commit=True):
        user = super(AccountCreateForm, self).save(commit=False)
        user.save()
        user_profile = Account(user=user)

        if commit:
            user_profile.save()

        return user_profile
