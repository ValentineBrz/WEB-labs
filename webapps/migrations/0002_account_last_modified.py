# Generated by Django 4.1.7 on 2023-06-26 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
