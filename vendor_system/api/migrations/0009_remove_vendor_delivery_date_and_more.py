# Generated by Django 5.0.5 on 2024-05-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_vendor_time_delivery_vendor_delivery_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='delivery_date',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='fulfillment',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='quality_rating',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='response_time',
        ),
        migrations.AddField(
            model_name='vendor',
            name='fulfillment_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='response_time_rate',
            field=models.FloatField(null=True),
        ),
    ]