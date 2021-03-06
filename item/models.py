import datetime
from django.utils import timezone
from django.db import models
from django.conf import settings

class Closet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE,null=True)
    closet_name = models.CharField(verbose_name='クローゼット名', max_length=255)
    closet_memo = models.CharField(verbose_name='メモ', max_length=325)
    create_date = models.DateTimeField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        ordering = ['closet_name']

    def __str__(self):
        return self.closet_name

    @property
    def item_count(self):
        item_count= Item.objects.filter(closet=self).count()
        return item_count



ITEM_TYPE_CHOICES = [('jacket','上着'),('shirt','シャツ'),('pants','パンツ'),('underpants','下着(下)'),('undershirt','下着(上)'),('socks','靴下'),('others','その他')]
SEASON_CHOICES = [('spring','春'),('summer','夏'),('fall','秋'),('winter','冬')]
OCCASION_CHOICES = [('daily_use','普段着'),('work_wear','仕事'),('active_wear','よそ行き'),('sports_wear','スポーツ'),('other_use','その他')]
ITEM_COLOR_CHOICES = [('red','赤'),('blue','青'),('green','緑'),('yellow','黄'),('purple','紫'),('orange','橙'),('black','黒'),('white','白'),('grey','灰'),('beige','ベージュ'),('navy','ネイビー'),('brown','茶'),('others','その他')]
FAVORITE_LEVEL_CHOICES = [(1,'めちゃ低い'),(2,'低い'),(3,'普通'),(4,'高い'),(5,'めちゃ高い')]
ITEM_IMPORTANCE_CHOICES = [(1,'捨てれる'),(2,'悩む'),(3,'普通'),(4,'まあ大事'),(5,'めっちゃ大事')]

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE,null=True)
    data_id = models.AutoField(verbose_name = 'アイテムNo.', primary_key=True)
    item_type = models.CharField(verbose_name = 'アイテム種類', max_length=255, choices = ITEM_TYPE_CHOICES)
    season = models.CharField(verbose_name = '季節', max_length=10, choices = SEASON_CHOICES, default='spring')
    occasion = models.CharField(verbose_name = 'シーン', max_length=30, choices = OCCASION_CHOICES, default='daily_use')
    item_name = models.CharField(verbose_name = 'アイテム名称', max_length=300)
    item_color = models.CharField(verbose_name = 'アイテム色', max_length=20, choices = ITEM_COLOR_CHOICES, blank=True, null=True)
    item_brand = models.CharField(verbose_name = 'ブランド', max_length=150, blank=True,null=True)
    purchase_date = models.DateTimeField(verbose_name = '購入日', blank=True, null=True)
    pricing = models.IntegerField(verbose_name = '購入価格(円)', )
    purchase_place = models.CharField(verbose_name = '購入場所', max_length=255,blank=True,null=True)
    item_image = models.ImageField(verbose_name = 'アイテム画像', upload_to='images/closet', blank = True, null=True)
    memo = models.TextField(verbose_name = 'メモ', blank=True,null=True)
    favorite_level = models.IntegerField(verbose_name = 'お気に入り度', choices = FAVORITE_LEVEL_CHOICES, blank=True, null=True, default='1')
    item_importance = models.IntegerField(verbose_name = '大事さ', choices = ITEM_IMPORTANCE_CHOICES, blank=True, null=True, default='1')
    create_date = models.DateTimeField(verbose_name = '作成日', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name = '更新日', auto_now=True)
    closet = models.ForeignKey(Closet, on_delete=models.PROTECT, null=True, default=None)

    class Meta:
        ordering = ['purchase_date']

    @property
    def aging_date(self):
        purchase_date = self.purchase_date
        gap_date = timezone.now() - purchase_date
        return (gap_date)

    @property
    def item_count_item(self):
        item_count_item = Item.objects.filter(item_type=self).count()
        return item_count_item

    @property
    def total_amount(self):
        pricing = self.pricing
        return (pricing)
    
    def __str__(self):
        return self.item_name












