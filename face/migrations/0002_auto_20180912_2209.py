# Generated by Django 2.1.1 on 2018-09-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='emotionCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='emotionData',
            field=models.TextField(default=''),
        ),
    ]
