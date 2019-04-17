from django import forms

class messageform(forms.Form):
	"""docstring for form"""

	title = forms.CharField(max_length = 300)
	description = forms.CharField(widget = forms.Textarea)
