# Generated by Django 3.1.2 on 2021-07-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0008_auto_20210703_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectoffered',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
