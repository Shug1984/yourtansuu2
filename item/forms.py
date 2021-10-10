from django import forms
from django.core.exceptions import ValidationError
from django.views.generic.edit import CreateView
from django.conf import settings

from .models import Item, Closet, FAVORITE_LEVEL_CHOICES, ITEM_IMPORTANCE_CHOICES


MONTHS = {
    1: '1月', 2: '2月', 3: '3月', 4: '4月',
    5: '5月', 6: '6月', 7: '7月', 8: '8月',
    9: '9月', 10: '10月', 11: '11月', 12: '12月'
}


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_name','item_type','season','occasion','pricing','purchase_date','closet','item_color','item_brand','purchase_place',
        'item_image','favorite_level','item_importance', 'memo',)

        labels = {'item_name':'アイテム名称(※必須)','item_type':'アイテム種類(※必須)','season':'季節(※必須)','occasion':'シーン(※必須)','pricing':'購入価格(円)(※必須)',
        'purchase_date':'購入日(※必須)','closet':'クローゼット','item_color':'アイテムカラー','item_brand':'ブランド','purchase_place':'購入場所','item_image':'アイテム画像',
        'favorite_level':'お気に入り度','item_importance':'大事さ','memo':'メモ',}

        widgets = {
            
            'purchase_date': forms.SelectDateWidget(years = [x for x in range(2000,2040)], months = MONTHS),
            'favorite_level': forms.RadioSelect(choices = FAVORITE_LEVEL_CHOICES ),
            'item_importance': forms.RadioSelect(choices = ITEM_IMPORTANCE_CHOICES),
        }
    
    def clean_closet(self):
        closet = self.cleaned_data['closet']
        if closet:
            closet_number = Item.objects.filter(closet=closet).count()
            if closet_number > settings.CLOSET_MAX:
                self.add_error('closet',f"クローゼットに登録出来るアイテムは{settings.CLOSET_MAX}件までです。")
        return closet


class ClosetForm(forms.ModelForm):
    class Meta:
        model = Closet
        fields = ('closet_name','closet_memo')
        labels = {'closet_name':'クローゼット名','closet_memo':'クローゼットメモ'}


class SearchForm(forms.Form):
    input_form = forms.CharField(max_length=100, label='検索',required=False)

    sort_form = forms.ChoiceField(
        choices = (
            ('','指定なし'),
            ('purchase_date','経過時間：古い順'),
            ('-purchase_date','経過時間:新しい順'),
            ('-pricing','購入価格:高い順'),
            ('pricing','購入価格:安い順'),
            ),
        label = '並べ替え',
        required=False,
        )

    