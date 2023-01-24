# Generated by Django 4.1.5 on 2023-01-24 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reading_groups", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="readinggrouphasuser",
            name="user",
            field=models.ForeignKey(
                default=3,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]