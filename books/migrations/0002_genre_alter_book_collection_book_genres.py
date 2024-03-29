# Generated by Django 4.1.2 on 2022-11-16 12:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name="book",
            name="collection",
            field=models.CharField(max_length=64),
        ),
        migrations.AddField(
            model_name="book",
            name="genres",
            field=models.ManyToManyField(to="books.genre"),
        ),
    ]
