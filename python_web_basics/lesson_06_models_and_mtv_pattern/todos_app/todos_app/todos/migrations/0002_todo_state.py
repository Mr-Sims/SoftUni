# Generated by Django 3.2.4 on 2021-06-04 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
