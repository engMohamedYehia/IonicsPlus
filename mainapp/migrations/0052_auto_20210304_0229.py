# Generated by Django 3.1.6 on 2021-03-04 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0051_auto_20210304_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_service',
            name='payment_link_Knet',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='payment_link_visa',
            field=models.CharField(max_length=300, null=True),
        ),
    ]