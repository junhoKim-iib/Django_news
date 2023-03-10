# Generated by Django 4.1.7 on 2023-03-12 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("analysis", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MainSentiment",
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
                ("sentiment", models.IntegerField()),
                (
                    "url",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="analysis.mainnews",
                    ),
                ),
            ],
            options={
                "db_table": "main_sentiment",
            },
        ),
    ]
