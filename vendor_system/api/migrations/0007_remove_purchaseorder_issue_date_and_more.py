# Generated by Django 5.0.5 on 2024-05-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_vendor_vendor_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='issue_date',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='average_response_time',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='fulfillment_rate',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='on_time_delivery_rate',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='quality_rating_avg',
        ),
        migrations.AddField(
            model_name='vendor',
            name='fulfillment',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='quality_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='response_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='time_delivery',
            field=models.BooleanField(null=True),
        ),
    ]