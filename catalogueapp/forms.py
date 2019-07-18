from django import forms
from catalogueapp.models import Organisation


class AddForm(forms.Form):
    url = forms.URLField(label='URL')


class EditOrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ('our_description_markdown',)
