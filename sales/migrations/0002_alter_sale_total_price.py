# Generated by Django 5.0.7 on 2024-07-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total_price',
            field=models.FloatField(blank=True, null=2),
        ),
    ]
