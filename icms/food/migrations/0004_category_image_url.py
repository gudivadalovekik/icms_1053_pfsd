# Generated by Django 4.2.6 on 2023-11-04 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_category_parent_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
