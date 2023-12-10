# Generated by Django 4.2.7 on 2023-12-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discussions", "0003_remove_reply_created_by_delete_discussion_and_more"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UCS_User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "linkedin_url",
                    models.URLField(blank=True, default="", max_length=300),
                ),
                ("github_url", models.URLField(blank=True, default="", max_length=300)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]