# Generated by Django 5.0.6 on 2024-05-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_management', '0002_remove_alerts_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='status',
            field=models.CharField(choices=[('working', 'Working'), ('under_repair', 'Under Repair'), ('in_storage', 'In Storage')], max_length=50),
        ),
    ]