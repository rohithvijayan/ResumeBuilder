from django import forms
from .models import resume
class resumeForm(forms.ModelForm):
    class Meta:
        model=resume
        fields='__all__'