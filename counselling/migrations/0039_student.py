# Generated by Django 3.1.2 on 2021-08-26 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0038_auto_20210826_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(max_length=220)),
            ],
        ),
    ]