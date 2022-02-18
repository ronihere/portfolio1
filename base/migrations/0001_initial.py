# Generated by Django 3.2.5 on 2022-02-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(default='none', max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]