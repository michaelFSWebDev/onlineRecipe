# Generated by Django 4.0.4 on 2022-04-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeApp', '0002_recipe_recipe_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_category',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
