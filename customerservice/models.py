from django.conf import settings
from django.db import models

RESPONSE_SPEED = [('express','超急ぎ'),('quick','急ぎ'),('standard','普通'),('slow','急ぎません')]

class Inquiry(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name ="投稿者", on_delete=models.CASCADE)
    title = models.CharField('タイトル', max_length=155)
    content = models.TextField('内容', blank=True)
    requested_response = models.CharField('回答スピードの希望', choices=RESPONSE_SPEED, max_length=100)
    created_at = models.DateTimeField("質問日", auto_now_add=True)

    def __str__(self):
        return self.title



# Create your models here.
