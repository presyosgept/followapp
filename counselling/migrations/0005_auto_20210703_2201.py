# Generated by Django 3.1.2 on 2021-07-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0004_auto_20210703_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counselorschedule',
            name='service_offered',
            field=models.CharField(choices=[('CLASS', 'CLASS'), ('COUNSELING', 'COUNSELING'), ('OTHERS', 'OTHERS')], max_length=220),
        ),
    ]
