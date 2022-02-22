# Generated by Django 3.1.2 on 2021-12-10 13:39

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0128_auto_20211209_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersreferral',
            name='behavior_problem',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('CHEATING', 'CHEATING'), ('TARDINESS', 'TARDINESS'), ('DISRESPECTFUL', 'DISRESPECTFUL'), ('ATTITUDE', 'ATTITUDE'), ('USING GADGETS IN CLASS', 'USING GADGETS IN CLASS'), ('GRUBBING', 'GRUBBING'), ('OTHERS', 'OTHERS')], max_length=220, null=True),
        ),
    ]