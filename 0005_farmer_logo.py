# Generated by Django 3.1.5 on 2021-06-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkulima', '0004_auto_20210603_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='logo',
            field=models.FileField(default='logos/logo.png', upload_to='logos'),
        ),
    ]
