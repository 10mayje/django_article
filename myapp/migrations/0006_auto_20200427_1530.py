# Generated by Django 3.0.4 on 2020-04-27 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_auto_20200427_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='commtno',
            field=models.CharField(blank=0, default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='likeno',
            field=models.CharField(blank=0, default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Blog'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]