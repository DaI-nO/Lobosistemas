from django.db import models
from work_orders.models import WorkOrder


class AdditionalCost(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    cost_description = models.TextField()
    cost_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()


class TotalCost(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    parts_material_cost = models.DecimalField(max_digits=10, decimal_places=2)
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    additional_cost = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total_wo_cost = models.DecimalField(max_digits=10, decimal_places=2)
