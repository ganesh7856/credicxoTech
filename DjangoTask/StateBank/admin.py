from django.contrib import admin
from StateBank.models import Branch_Name

# Register your models here.


class Branch_NameAdmin(admin.ModelAdmin):
        list_display=['bank','branch_name','ifsc_code','address','city','district','state']




admin.site.register(Branch_Name,Branch_NameAdmin)
