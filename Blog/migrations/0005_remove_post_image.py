# Generated by Django 3.0.4 on 2020-04-09 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20200409_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
