# Generated by Django 3.1.6 on 2021-02-23 12:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210222_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_service',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
