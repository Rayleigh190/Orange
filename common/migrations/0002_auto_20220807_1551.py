# Generated by Django 3.1.6 on 2022-08-07 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follower',
            field=models.ManyToManyField(blank=True, related_name='_profile_follower_+', to='common.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='_profile_following_+', to='common.Profile'),
        ),
    ]
