# Generated by Django 4.0.4 on 2022-04-23 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_returns_delete_statustype'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Returns',
            new_name='Return',
        ),
    ]
