# Generated by Django 5.0.3 on 2024-03-14 12:11

from django.db import migrations
from apps.corecode.models import User
import datetime


def default_site_config(apps, schema_editor):
    """Default site configurations"""

    User.objects.create_superuser("vdmcsc", "vdmcsc4@gmail.com", "606001")
    Config = apps.get_model("corecode", "SiteConfig")
    Config.objects.bulk_create(
        [
    
            Config(key="Institute", value="COMPUTER SOFTWARE COLLEGE"),
        ]
    )

    Session = apps.get_model("corecode", "AcademicSession")
    Session.objects.bulk_create(
        [
            Session(name="Annamalai Nagar", current=True),
        ]
    )

    Term = apps.get_model("corecode", "AcademicTerm")
    Term.objects.bulk_create(
        [
            Term(name=f"{datetime.datetime.now().year}", current=True),
        ]
    )

    Subject = apps.get_model("corecode", "Subject")

    StudentClass = apps.get_model("corecode", "StudentClass")
    StudentClass.objects.bulk_create(
        [
            StudentClass(name="HDCA"),
            StudentClass(name="DCA"),
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(default_site_config),
    ]
