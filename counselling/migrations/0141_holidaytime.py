# Generated by Django 3.1.2 on 2022-02-23 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0140_auto_20220222_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='holidaytime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_date', models.DateField()),
            ],
        ),
    ]
