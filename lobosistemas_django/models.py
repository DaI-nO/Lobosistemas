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

class TaskDetails(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    assigned_to = models.CharField(max_length=255)
    note = models.TextField()

class PartsMaterial(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    article_number = models.CharField(max_length=50)
    article_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    article_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()

class LaborDetails(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    worker_name = models.CharField(max_length=255)
    work_code = models.CharField(max_length=50)
    speed = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()

class Observations(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    observation = models.TextField()
    date = models.DateTimeField()
    observer = models.CharField(max_length=255)

class AdditionalCost(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    cost_description = models.TextField()
    cost_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()

class AttachedFiles(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    description = models.TextField()
    file_path = models.TextField()

class TotalCost(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    parts_material_cost = models.DecimalField(max_digits=10, decimal_places=2)
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    additional_cost = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total_wo_cost = models.DecimalField(max_digits=10, decimal_places=2)
