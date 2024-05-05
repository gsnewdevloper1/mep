from django.contrib import admin
from myapp.models import pending_work , work_details , contactus

# Register your models here.
admin.site.register(pending_work)
admin.site.register(work_details)
admin.site.register(contactus)
