# Generated by Django 5.0.5 on 2024-05-10 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_purchaseorder_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
