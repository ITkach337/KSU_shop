# Generated by Django 3.2.8 on 2022-07-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('caps', 'caps'), ('t_shirts', 't_shirts'), ('cups', 'cups'), ('pens', 'pens')], max_length=30, verbose_name='Категории'),
        ),
    ]