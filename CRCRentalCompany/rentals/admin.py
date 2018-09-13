from django.contrib import admin

from.models import Order
from.models import Customer
from.models import Vehicle
from.models import Store

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ["orderCreateDate", "pickupDate", "returnDate",
		"customerId", "carId", "pickupStoreId", "returnStoreId"]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ["customerName", "customerPhone", "customerAddress",
		"customerBirthday", "customerOccupation", "customerGender"]

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
	list_display = ["make", "model", "series", "year", "price",
		"engine", "fuelType", "tankCapacity", "power", "seats",
		"transmission", "bodyType", "driveType", "wheelbase"]

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
	list_display = ["storeName"]
