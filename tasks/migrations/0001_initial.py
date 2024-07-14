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
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('assigned_to', models.CharField(max_length=255)),
                ('note', models.TextField()),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_orders.workorder')),
            ],
        ),
    ]
