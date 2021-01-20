from django import forms
from django.core.exceptions import ValidationError
from .models import *

class ImageForm(forms.ModelForm):
    class Meta():
        model = Image
        fields = ('image',)

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if not self.instance.image == image:
            # validate image
            print()
        return None

class SearchForm(forms.Form):
    user_id = forms.CharField(
        initial='',
        label='user id',
        required=False,  # 必須ではない
    )
    title = forms.CharField(
        initial='',
        label='title',
        required = False, # 必須ではない
    )
    text = forms.CharField(
        initial='',
        label='date',
        required=False,  # 必須ではない
    ) 