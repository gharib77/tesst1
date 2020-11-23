from django import forms
from app1.models import Personne
class FormPers(forms.ModelForm):
    class Meta:
        model=Personne
        fields=('nom','prenom','grade','date_nais')