# Generated by Django 2.1.15 on 2022-10-30 10:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imageThumb',
            field=models.ImageField(blank=True, upload_to='movieThumb'),
        ),
        migrations.AddField(
            model_name='movie',
            name='imgUrl',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 10, 30, 10, 11, 45, 984187, tzinfo=utc)),
            preserve_default=False,
        ),
    ]