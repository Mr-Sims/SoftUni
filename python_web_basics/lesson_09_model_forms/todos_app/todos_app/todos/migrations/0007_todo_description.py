# Generated by Django 3.2.4 on 2021-06-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_auto_20210606_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(null=True),
        ),
    ]