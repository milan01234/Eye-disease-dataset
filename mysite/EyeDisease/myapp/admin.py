from django.contrib import admin
from myapp.models import Patient
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display=('Patient_Name','Xender','Age','Eye_Image','Disease')
admin.site.register(Patient,PatientAdmin)