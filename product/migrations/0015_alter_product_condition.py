# Generated by Django 3.2.5 on 2021-09-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used'), ('Sold', 'Sold')], max_length=100),
        ),
    ]
