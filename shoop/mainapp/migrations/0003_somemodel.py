# Generated by Django 4.0.4 on 2022-05-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_smartphone_notebook'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
