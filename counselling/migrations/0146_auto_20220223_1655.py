# Generated by Django 3.1.2 on 2022-02-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0145_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickedDate', models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
    ]
