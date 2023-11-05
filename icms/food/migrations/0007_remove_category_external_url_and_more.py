# Generated by Django 4.2.6 on 2023-11-04 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_remove_fooditem_category_delete_street_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='external_url',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent_category',
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('famous_foods', models.TextField()),
                ('average_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.category')),
            ],
        ),
    ]
