# Generated by Django 3.1.2 on 2021-11-19 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0115_auto_20211116_2300'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompareTime',
        ),
        migrations.DeleteModel(
            name='NewTime',
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]