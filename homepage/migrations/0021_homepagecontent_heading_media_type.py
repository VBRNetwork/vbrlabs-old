# Generated by Django 3.1.5 on 2022-05-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0020_auto_20220517_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecontent',
            name='heading_media_type',
            field=models.CharField(blank=True, choices=[('image', 'Image'), ('video', 'Video')], max_length=255),
        ),
    ]
