# Generated by Django 3.0 on 2020-08-05 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0006_auto_20200804_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='allview',
            name='desc',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='allview',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
