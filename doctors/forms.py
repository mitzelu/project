from django import forms

class SearchDoc(forms.Form):
	specialization = forms.CharField(max_length=20)
	zip_code  = forms.CharField(max_length=20)


class BookDoc(forms.Form):
	firstName = forms.CharField(max_length=50)
	lastName  = forms.CharField(max_length=50)
	phone     = forms.CharField(max_length=50)
	email     = forms.CharField(max_length=50)
