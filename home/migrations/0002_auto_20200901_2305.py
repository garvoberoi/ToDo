# Generated by Django 3.0.7 on 2020-09-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
