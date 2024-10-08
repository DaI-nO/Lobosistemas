# Generated by Django 5.0.7 on 2024-07-14 22:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('work_orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_number', models.CharField(max_length=50)),
                ('article_name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('article_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.TextField()),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_orders.workorder')),
            ],
        ),
    ]
