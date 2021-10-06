# Generated by Django 3.1.2 on 2021-08-26 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0033_schooloffices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.IntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=220)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselling.schooloffices')),
            ],
        ),
    ]