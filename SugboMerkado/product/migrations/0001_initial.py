# Generated by Django 3.1.1 on 2020-10-15 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRegistered', models.DateField(auto_now=True)),
                ('sku', models.CharField(max_length=6)),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=25)),
                ('unitPrice', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('isdeleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productImage', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'Product_Images',
            },
        ),
    ]
