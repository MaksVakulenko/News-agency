from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from newspaper.models import Newspaper, Redactor


class NewspaperForm(forms.ModelForm):
    publishing_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        initial=timezone.now,
    )

    class Meta:
        model = Newspaper
        fields = ["title", "content", "publishing_date", "topics", "publishers"]


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )
