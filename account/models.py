from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("メールアドレスを登録してください")
        
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password = password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

GENDER_CHOICES = [('male','男性'),('female','女性'),('not_applicable','無回答')]
REGION_NAME_CHOICES = [('hokkaido', '北海道'), ('aomori', '青森県'), ('iwate', '岩手県'), ('miyagi', '宮城県'), ('akita', '秋田県'), ('yamagata', '山形県'), 
('fukushima', '福島県'), ('ibaraki', '茨城県'), ('tochigi', '栃木県'), ('gunma', '群馬県'), ('saitama', '埼玉県'), ('chiba', '千葉県'), ('tokyo', '東京都'), 
('kanagawa', '神奈川県'), ('niigata', '新潟県'), ('toyama', '富山県'), ('ishikawa', '石川県'), ('fukui', '福井県'), ('yamanashi', '山梨県'), 
('nagano', '長野県'), ('gifu', '岐阜県'), ('shizuoka', '静岡県'), ('aichi', '愛知県'), ('mie', '三重県'), ('shiga', '滋賀県'), ('kyoto', '京都府'), 
('osaka', '大阪府'), ('hyogo', '兵庫県'), ('nara', '奈良県'), ('wakayama', '和歌山県'), ('tottori', '鳥取県'), ('shimane', '島根県'), ('okayama', '岡山県'), 
('hiroshima', '広島県'), ('yamaguchi', '山口県'), ('tokushima', '徳島県'), ('kagawa', '香川県'), ('ehime', '愛媛県'), ('kochi', '高知県'), ('fukuoka', '福岡県'), 
('saga', '佐賀県'), ('nagasaki', '長崎県'), ('kumamoto', '熊本県'), ('oita', '大分県'), ('miyazaki', '宮崎県'), ('kagoshima', '鹿児島県'), ('okinawa', '沖縄県'),('kaigai','海外その他')]


class MyUser(AbstractBaseUser):
    email = models.CharField(max_length=50, unique= True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_kana = models.CharField(max_length=100)
    first_kana = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    region_name = models.CharField(max_length=100, choices=REGION_NAME_CHOICES)
    city_name= models.CharField(max_length=100)
    street_name= models.CharField(max_length=100)
    building_name= models.CharField(max_length=300)
    tel = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
 
    def has_module_perms(self, app_label):
        return True
 
    @property
    def is_staff(self):
        return self.is_admin

