from django.db import models
from work_orders.models import WorkOrder


class LaborDetail(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    worker_name = models.CharField(max_length=255)
    work_code = models.CharField(max_length=50)
    speed = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()
