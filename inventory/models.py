from django.db import models
from work_orders.models import WorkOrder


class PartMaterial(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    article_number = models.CharField(max_length=50)
    article_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    article_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()
