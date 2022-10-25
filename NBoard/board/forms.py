from django import forms

from .models import Ad, Response


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = [
            'category',
            'title',
            'text',
            'uploads',
        ]

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'text',
        ]

