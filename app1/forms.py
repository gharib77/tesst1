from django import forms
from app1.models import Personne,Ecrivain,Book,Produit
from django.utils.translation import gettext, gettext_lazy as _
class FormEcr(forms.ModelForm):
    class Meta:
        model=Ecrivain
        fields=['name','age']
        labels = {'name': _('New date')}
        widgets = {
			'name': forms.TextInput(attrs={'class': 'formset-field'}),
			'age': forms.TextInput(attrs={'class': 'formset-field'}),
		}

class FormBook(forms.ModelForm):
    class Meta:
        model=Book
        fields=['name','isbn_number']
        widgets = {
			'name': forms.TextInput(attrs={'class': 'formset-field'}),
			'isbn_number': forms.TextInput(attrs={'class': 'formset-field'}),
		}


class FormPers(forms.ModelForm):
    nom=forms.CharField(max_length=40,
    widget= forms.TextInput(attrs={'class':'vnom'}))
    date_of_birth = forms.DateField(input_formats=['%d/%m/%Y'],
    widget=forms.DateInput(attrs={'class':'cdate1'}))
    date_of_death = forms.DateField(input_formats=['%d/%m/%Y'],
    widget=forms.DateInput(attrs={'class':'cdate1'}))
    date_nais=forms.DateField(input_formats=['%d/%m/%Y'],
    widget=forms.DateInput(attrs={'class':'cdate1'},format='%d/%m/%Y'))
    class Meta:
        model=Personne
        fields=('nom','prenom','grade','date_nais')
    """def clean_nom(self):
        wnom_value = self.cleaned_data['nom']
        if 'fathi' not in wnom_value:
            raise forms.ValidationError('soruuuuuuuuuu')
        return  wnom_value
    """
    def clean(self):
        cleaned_data = super().clean()
        date_of_birth = cleaned_data.get('date_of_birth')
        date_of_death = cleaned_data.get('date_of_death')
        if date_of_birth and date_of_death and date_of_birth > date_of_death:
            raise forms.ValidationError('Birth date must be before death date.')
        return cleaned_data

class FormProd(forms.ModelForm):
    date_entr=forms.DateTimeField(input_formats=['%d/%m/%Y'],
    widget=forms.DateTimeInput(format='%d/%m/%Y'))
    class Meta:
        model=Produit
        fields='__all__'