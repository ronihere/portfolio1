# Generated by Django 3.2.5 on 2022-02-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='link',
            field=models.URLField(default='www.google.com'),
        ),
    ]
