from django import forms
from django.core.exceptions import ValidationError
from .models import *

# class UserForm(forms.Form):
#     name = forms.CharField(label='name',widget=forms.TextInput(attrs={'class':'form-control'}))

# class ImageForm(forms.Form):
#     f_name = forms.CharField(label='file',widget=forms.TextInput(attrs={'class':'form-control'}))

# class WordForm(forms.Form):
#     dialogue = forms.CharField(label='dialogue',widget=forms.TextInput(attrs={'class':'form-control'}))
#     attribute = forms.CharField(label='attribute',widget=forms.TextInput(attrs={'class':'form-control'}))

# class PaintingForm(forms.Form):
#     user_id = forms.CharField(label='user_id',widget=forms.TextInput(attrs={'class':'form-control'}))
#     title = forms.CharField(label='title',widget=forms.TextInput(attrs={'class':'form-control'}))
#     f_name = forms.CharField(label='file',widget=forms.TextInput(attrs={'class':'form-control'}))

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
    def clean_user(self):
        name = self.cleaned_data.get('name',False)
        if not self.instance.name == name:
            # validate image
            print()
        return None

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
        

# class WordForm(forms.ModelForm):
#     class Meta():
#         model = Word
#         fields = '__all__'
    
#     def clean_word(self):
#         word = self.cleaned_data.get('words', False)
#         attribute = self.cleaned_data.get('attribute',False)
#         if not self.instance.words == word:
#             # validate image
#             print()
#         return None
#         if not self.instance.attribute == attribute:
#             # validate image
#             print()
#         return None

class PaintingForm(forms.ModelForm):
    class Meta():
        model = Painting
        fields = ('user_id','title','painting',)

    def clean_painting(self):
        painting = self.cleaned_data.get('painting', False)
        title = self.cleaned_data.get('title',False)
        user_id = self.cleaned_data.get('user_id',False)
        if not self.instance.painting == painting:
            # validate image
            print()
        return None
        if not self.instance.title == title:
            # validate image
            print()
        return None
        if not self.instance.user_id == user_id:
            # validate image
            print()
        return None