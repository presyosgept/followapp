# Generated by Django 3.1.2 on 2021-10-14 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0097_auto_20211014_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='load',
            fields=[
                ('id', models.CharField(max_length=220, primary_key=True, serialize=False)),
                ('employee_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='counselling.faculty')),
                ('offer_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='counselling.offercode')),
            ],
        ),
    ]
