from django.contrib import admin
from .models import WorkOrder, TaskDetails, PartsMaterial, LaborDetails, Observations, AdditionalCost, AttachedFiles, TotalCost

admin.site.register(WorkOrder)
admin.site.register(TaskDetails)
admin.site.register(PartsMaterial)
admin.site.register(LaborDetails)
admin.site.register(Observations)
admin.site.register(AdditionalCost)
admin.site.register(AttachedFiles)
admin.site.register(TotalCost)
