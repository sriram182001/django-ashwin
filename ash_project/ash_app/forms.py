from django import forms
from ash_app.models import UserPhoto
class FormPhoto(forms.ModelForm):
    class Meta:
        model=UserPhoto
        fields='__all__'
