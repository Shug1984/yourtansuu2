# Generated by Django 3.2.5 on 2021-08-17 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Closet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closet_name', models.CharField(max_length=255, verbose_name='クローゼット名')),
                ('closet_memo', models.CharField(max_length=325, verbose_name='メモ')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='closet',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='item.closet', verbose_name='クローゼット'),
        ),
    ]
