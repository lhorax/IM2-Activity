# Generated by Django 3.1.1 on 2020-10-06 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePurchased', models.DateField(auto_now_add=True)),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.person')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'Purchase',
            },
        ),
    ]