# Generated by Django 3.1.6 on 2021-02-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0037_auto_20210227_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_service',
            name='in_progress',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=False, max_length=75),
        ),
    ]
