# Generated by Django 3.1.2 on 2022-04-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0158_auto_20220405_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counselor',
            name='program_designation',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
