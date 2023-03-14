from django.contrib import admin
from first_app.models import truck_driver, seller_details, truck_details

# Register your models here.
admin.site.register(truck_driver)
admin.site.register(seller_details)
admin.site.register(truck_details)
