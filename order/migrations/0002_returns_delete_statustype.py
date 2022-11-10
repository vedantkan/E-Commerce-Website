# Generated by Django 4.0.4 on 2022-04-23 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Returns',
            fields=[
                ('return_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=20)),
                ('return_reason', models.CharField(max_length=100)),
                ('fk_details', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='order.orderdetail')),
            ],
            options={
                'ordering': ('return_id',),
            },
        ),
        migrations.DeleteModel(
            name='StatusType',
        ),
    ]