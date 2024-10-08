# Generated by Django 5.1 on 2024-08-23 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("batch", "0002_initial"),
        ("staffs", "0004_alter_staff_pincode"),
        ("students", "0006_student_m_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="batchmodel",
            name="batch_staff",
            field=models.ForeignKey(
                limit_choices_to={"current_status": "active"},
                on_delete=django.db.models.deletion.PROTECT,
                to="staffs.staff",
            ),
        ),
        migrations.AlterField(
            model_name="batchmodel",
            name="batch_students",
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={"current_status": "active"},
                to="students.student",
            ),
        ),
    ]
