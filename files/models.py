from django.db import models
from work_orders.models import WorkOrder


class AttachedFile(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    description = models.TextField()
    file_path = models.TextField()
