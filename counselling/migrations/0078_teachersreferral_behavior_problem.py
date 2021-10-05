# Generated by Django 3.1.2 on 2021-09-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0077_delete_referrals'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachersreferral',
            name='behavior_problem',
            field=models.CharField(blank=True, choices=[('CHEATING', 'CHEATING'), ('TARDINESS', 'TARDINESS'), ('DISRESPECTFUL', 'DISRESPECTFUL'), ('ATTITUDE', 'ATTITUDE'), ('USING GADGETS IN CLASS', 'USING GADGETS IN CLASS'), ('GRUBBING', 'GRUBBING')], max_length=220, null=True),
        ),
    ]
