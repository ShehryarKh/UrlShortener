from django import forms
from django.models import UrlField

class UrlForm(forms.ModelForm):
	class Meta:
		model = UrlField

		fields = [
		'field',
		]