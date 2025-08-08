from django import forms
from .models import SoilData

class SoilDataForm(forms.ModelForm):
    class Meta:
        model = SoilData
        fields = '__all__'
