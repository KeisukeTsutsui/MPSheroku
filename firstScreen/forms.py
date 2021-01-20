from django import forms
from .myImagePoint_Edited import PaintingCreate
from .models import Member#, Painting


class ModelForm(forms.ModelForm):
    class Meta():
        model = Member
        fields = ('title', 'text', 'ballon_type', 'font_size', 'point_x', 'point_y')
        labels = {
            'title'         :'題名',
            'text'          :'テキスト',
            'ballon_type'   :'風船の向き', 
            # 'ballon_height' :'風船の大きさ(縦)', 
            # 'ballon_wight'  :'風船の大きさ(横)', 
            'font_size'     :'文字の大きさ',
            'point_x'       :'x座標', 
            'point_y'       :'y座標',
            # 'painting_name' :'画像の名前'
        }
    
    def Create(self, painting):
        content = (
            self.cleaned_data['title'],
            self.cleaned_data['text'],
            self.cleaned_data['ballon_type'],
            # self.cleaned_data['ballon_height'],
            # self.cleaned_data['ballon_wight'],
            self.cleaned_data['font_size'],
            self.cleaned_data['point_x'],
            self.cleaned_data['point_y']
        )
        PaintingCreate.merge(content, painting)
""" 
class BallonForm(forms.Form):
    BALLON_TYPE = (
        ('1', '左下'),
        ('2', '左上'),
        ('3', '右下'),
        ('4', '右上'),
    )
    FONT_SIZE = (
        ('1', '大'),
        ('2', '中'),
        ('3', '小'),
    )

    text = forms.CharField(max_length=50, initial='message here', required=True)
    ##ballon_type = forms.ChoiceField(BALLON_TYPE, initial='1', required=True, widget=forms.widgets.Select)
    ##font_size = forms.ChoiceField(FONT_SIZE, initial='2', required=True, widget=forms.widgets.Select)
    point_x = forms.IntegerField(max_value=680, initial=0, required=True)
    point_y = forms.IntegerField(max_value=480, initial=0, required=True)

class PaintingForm(forms.ModelForm):
    class Meta():
        model = Painting
        fields = ('title',)
        labels = {
            'title' :'題名',
        }
   """      
# class SampleForm(forms.ModelForm):
#     class Meta():
#         model = Member
#         fields = ('title', 'text', 'ballon_type', 'text2', 'ballon_type2')
#         labels = {
#             'title'         :'題名',
#             'text'          :'テキスト',
#             'ballon_type'   :'風船の向き', 
#             'text2'         :'テキスト２',
#             'ballon_type2'   :'風船の向き２'
#         }

    
#     def Create(self, painting):
#         size = {
#             'h1':'',
#             'w1':'',
#             'x1':'1200',
#             'y1':'1200',
#             'h2':'',
#             'w2':'',
#             'x2':'1200',
#             'y2':'1200'
#         }
#         content = (
#             self.cleaned_data['title'],
#             self.cleaned_data['text'],
#             self.cleaned_data['ballon_type'],
#             self.cleaned_data['ballon_height'],
#             self.cleaned_data['ballon_wight'],
#             self.cleaned_data['point_x'],
#             self.cleaned_data['point_y']
#         )
#         PaintingCreate.merge(content, painting)
