# Generated by Django 3.1.5 on 2022-02-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_otp_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='service_type',
            field=models.CharField(blank=True, choices=[('loan', 'Loan'), ('deposit', 'Deposit')], max_length=255, null=True),
        ),
    ]
