# Generated by Django 3.1.6 on 2022-08-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20220807_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follower',
            field=models.ManyToManyField(blank=True, to='common.Profile'),
        ),
    ]
