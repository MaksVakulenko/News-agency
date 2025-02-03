from django import forms
from django.utils import timezone
from .models import Newspaper


class NewspaperForm(forms.ModelForm):
    pub_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        initial=timezone.now,
    )

    class Meta:
        model = Newspaper
        fields = ["title", "content", "pub_date", "topic", "publishers"]
