# Generated by Django 4.1.7 on 2023-04-05 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0003_alter_food_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='special_price',
            field=models.IntegerField(null=True),
        ),
    ]
