# Generated by Django 4.2.4 on 2023-09-28 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_ledger', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core_ledger.tag'),
        ),
    ]
