# Generated by Django 4.2.7 on 2023-11-13 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_ingredientrecipe_amount'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ingredientrecipe',
            unique_together={('recipe', 'ingredient')},
        ),
    ]