from django import forms

from .models import Image


class ImageFormModel(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'photo']

class UploadFileForm(forms.Form):
    #name = forms.CharField(max_length = 15)
    # files = forms.FileField()
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))