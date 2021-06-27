# Generated by Django 3.2.4 on 2021-06-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('ingredients', models.CharField(max_length=250)),
                ('time', models.IntegerField()),
            ],
        ),
    ]
