# Generated by Django 3.2.23 on 2024-01-25 16:33

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0006_auto_20240124_1647"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=["middle", "center"],
                force_format="WEBP",
                keep_meta=True,
                quality=75,
                scale=None,
                size=[400, 400],
                upload_to="recipes/",
            ),
        ),
    ]
