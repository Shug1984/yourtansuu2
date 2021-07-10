from django import forms
from .models import MyUser

class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = (
            'email','last_name','first_name','last_kana',
            'first_kana','zip_code','region_name','city_name',
            'street_name','building_name','tel','date_of_birth','gender'
        )

        labels = {
            'email':'メールアドレス','last_name':'姓','first_name':'名',
            'last_kana':'フリガナ(姓)','first_kana':'フリガナ(名)','zip_code':'郵便番号',
            'region_name':'都道府県','ciry_name':'市町村名','street_name':'丁目・番地',
            'building_name':'建物名','tel':'電話番号','date_of_birth':'生年月日','gender':'性別'
        }
            
        help_texts = {}
