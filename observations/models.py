from django.db import models
from work_orders.models import WorkOrder


class Observation(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    observation = models.TextField()
    date = models.DateTimeField()
    observer = models.CharField(max_length=255)
