# Generated by Django 3.1.6 on 2021-03-03 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0046_auto_20210304_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_service',
            name='payment_link',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
