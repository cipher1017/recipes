# Generated by Django 4.2.1 on 2023-05-18 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_ingredient_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.TextField(max_length=255),
        ),
    ]
