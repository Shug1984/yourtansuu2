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
    
class MyUser(AbstractBaseUser):
    email = models.CharField(max_length=50, unique= True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_kana = models.CharField(max_length=100)
    first_kana = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    region_name = models.CharField(max_length=100)
    city_name= models.CharField(max_length=100)
    street_name= models.CharField(max_length=100)
    building_name= models.CharField(max_length=300)
    tel = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=10)

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

