from django import forms

class ApiRequestForm(forms.Form):
    url = forms.URLField(label='Request URL', required=True)
    method = forms.ChoiceField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('DELETE', 'DELETE')])
    headers = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), required=False, help_text="Headers in JSON format")
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':5}), required=False, help_text="Body in JSON format")
