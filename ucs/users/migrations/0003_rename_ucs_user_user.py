# Generated by Django 4.2.7 on 2023-12-10 09:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_ucs_user_delete_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="UCS_User",
            new_name="User",
        ),
    ]
