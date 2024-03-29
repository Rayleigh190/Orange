# Generated by Django 3.1.6 on 2022-08-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20220807_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follower',
            field=models.ManyToManyField(blank=True, related_name='followings', to='common.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='common.Profile'),
        ),
    ]
