from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
 
from .models import MyUser
 
 
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)
 
    class Meta:
        model = MyUser
        fields = ('email',)
 
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("パスワードが一致しません")
        return password2
 
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
 
 
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
 
    class Meta:
        model = MyUser
        fields = ('email','password','last_name','first_name','last_kana','first_kana','zip_code','region_name','city_name',
            'street_name','building_name','tel','date_of_birth','gender','is_active', 'is_admin')
 
    def clean_password(self):
        return self.initial["password"]

class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        
        fields = (
            'email','password','last_name','first_name','last_kana',
            'first_kana','zip_code','region_name','city_name',
            'street_name','building_name','tel','gender'
        )

        labels = {
            'email':'メールアドレス','password':'パスワード','last_name':'姓','first_name':'名',
            'last_kana':'フリガナ(姓)','first_kana':'フリガナ(名)','zip_code':'郵便番号',
            'region_name':'都道府県','city_name':'市町村名','street_name':'丁目・番地',
            'building_name':'建物名','tel':'電話番号','gender':'性別'
        }
            
        help_texts = {}
