# Generated by Django 4.0.1 on 2022-01-05 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='home/'),
        ),
    ]
