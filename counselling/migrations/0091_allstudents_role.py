# Generated by Django 3.1.2 on 2021-10-13 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0090_auto_20211013_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='allstudents',
            name='role',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
