# Generated by Django 2.1.1 on 2018-09-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0003_auto_20180912_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='emotionData',
            field=models.TextField(default='{"happy": 0, "neutral": 0, "sad": 0, "angry": 0, "surprise": 0, "disgust": 0, "fear": 0}'),
        ),
    ]
