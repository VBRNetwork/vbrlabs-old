# Generated by Django 3.1.5 on 2022-05-19 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0021_homepagecontent_heading_media_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='project_counts',
        ),
        migrations.DeleteModel(
            name='ProjectsCount',
        ),
    ]
