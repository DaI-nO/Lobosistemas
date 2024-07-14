from django.db import models
from work_orders.models import WorkOrder


class Task(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    assigned_to = models.CharField(max_length=255)
    note = models.TextField()
