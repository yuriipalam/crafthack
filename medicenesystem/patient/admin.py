from django.contrib import admin
from . import models

class PatientAdmin(admin.ModelAdmin):
    list_display  = ('first_name', 'last_name', 'social_number', 'disease')
    # list_display = ('__all__',)

admin.site.register(models.Instruction)
admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.Pillow)
