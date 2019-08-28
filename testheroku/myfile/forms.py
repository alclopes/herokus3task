from django import forms
from .models import MyFile


class FileUploadForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=128)
    file = forms.ImageField()

    class Meta:
        model = MyFile
        fields = ['name', 'file']


