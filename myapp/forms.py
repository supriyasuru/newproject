from django import forms
from django.conf import settings
from .models import CsvImport
from .models import *

class FileForm(forms.ModelForm):
	files = forms.FileField(widget=forms.FileInput(attrs={'accept':'.csv, application/pdf, .xls'}))  #show only selected files in accept key on browsing file

	class Meta:
		model = CsvImport
		fields = ('files',)