# Generated by Django 4.2.14 on 2024-08-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0003_receipt_gst_amount_receipt_org_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipt",
            name="gst_amount",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="receipt",
            name="org_amount",
            field=models.FloatField(null=True),
        ),
    ]
