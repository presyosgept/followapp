# Generated by Django 3.1.2 on 2022-04-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0171_delete_depachoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time1', models.TimeField(blank=True, null=True)),
                ('time2', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
