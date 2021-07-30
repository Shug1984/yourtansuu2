from django import forms
from django.views.generic.edit import CreateView 

from .models import Closet

class ClosetForm(forms.ModelForm):
   

    class Meta:
        model = Closet
        fields = ('data_id','item_type','season','occasion','item_name','item_color','item_brand','purchase_date','pricing','purchase_place','memo','favorite_level','item_importance')

        labels = {'data_id':'アイテムNo.','item_type':'アイテム種類','season':'季節','occasion':'シーン','item_name':'アイテム名称','item_color':'アイテムカラー','item_brand':'ブランド','purchase_date':'購入日','pricing':'購入価格(円)','purchase_place':'購入場所','memo':'メモ','favorite_level':'お気に入り度','item_importance':'大事さ'}

"""
class ClosetNewCreation(CreateView):
    template_name = 'contents/closet_create.html'
    form_class = ClosetForm

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(ClosetNewCreation, self).form_valid(form)
"""
    