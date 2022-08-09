# Generated by Django 3.1.6 on 2022-08-07 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('persona', '0016_hidepersona'),
    ]

    operations = [
        migrations.AddField(
            model_name='hidepersona',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.profile'),
        ),
    ]