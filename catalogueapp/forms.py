from django import forms


class AddForm(forms.Form):
    url = forms.URLField(label='URL')
