from django.contrib import admin
from api.models import Company, Employee

# Register your models here.


# class CompanyAdmin(admin.ModelAdmin):
    # list_displays = ('name', 'location', 'type')
    
    
admin.site.register(Company)
admin.site.register(Employee)
