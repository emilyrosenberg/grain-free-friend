# Generated by Django 5.0.1 on 2024-01-20 10:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0003_recipe_method"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="cuisine_types",
        ),
        migrations.RemoveField(
            model_name="recipe",
            name="meal_type",
        ),
    ]
