# Generated by Django 4.0.4 on 2022-04-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rename_returns_return'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
