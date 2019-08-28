from django import forms
from .models import MyImage


class ImageUploadForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=128)
    image = forms.ImageField()

    class Meta:
        model = MyImage
        fields = ['name', 'image']

    # https://medium.com/the-geospatials/serve-django-static-media-files-on-aws-s3-part-2-d0e8578dd2db
    # def save(self):
    #     myimage = super(ImageUploadForm, self).save()
    #     return myimage

