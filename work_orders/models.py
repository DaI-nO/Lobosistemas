from django.db import models


class WorkOrder(models.Model):
    title = models.CharField(max_length=255)
    memorandum = models.TextField()
    priority = models.CharField(max_length=50)
    assigned_to = models.CharField(max_length=255)
    work_order_type = models.CharField(max_length=50)
    link_inspection = models.TextField()
    link_work_order = models.TextField()
    vehicle_number = models.CharField(max_length=50)
    vehicle_name = models.CharField(max_length=255)
    vehicle_model = models.CharField(max_length=255)
    meter_reading = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    estimated_time = models.DecimalField(max_digits=10, decimal_places=2)
