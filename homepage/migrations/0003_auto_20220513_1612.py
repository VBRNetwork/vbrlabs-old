# Generated by Django 3.1.5 on 2022-05-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20220513_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockchainContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('blockchain_title', models.CharField(blank=True, max_length=255)),
                ('blockchain_subtitle', models.CharField(blank=True, max_length=255)),
                ('blockchain_content', models.TextField(blank=True)),
                ('blockchain_button_text', models.CharField(blank=True, max_length=255)),
                ('blockchain_button_link', models.CharField(blank=True, max_length=255)),
                ('blockchain_button_link_target_blank', models.BooleanField(default=False)),
                ('blockchain_order', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'Blockchain Content',
                'verbose_name_plural': 'Blockchain Content',
                'ordering': ['blockchain_order'],
            },
        ),
        migrations.RenameModel(
            old_name='AbuotUs',
            new_name='AboutUs',
        ),
    ]