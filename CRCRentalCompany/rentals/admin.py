from django.contrib import admin

from.models import Order
from.models import Customer
from.models import Vehicle
from.models import Store

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ["order_create_date", "pickup_date", "return_date",
		"customer_id", "car_id", "pickup_store_id", "return_store_id"]
#"rentalId" Need for all if adding again

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ["customer_name", "customer_phone", "customer_address",
		"customer_birthday", "customer_occupation", "customer_gender"]

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
	list_display = ["make", "model", "series", "year", "price",
		"engine", "fuel_type", "tank_capacity", "power", "seats",
		"transmission", "body_type", "drive_type", "wheelbase"]

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
	list_display = ["store_name", "store_address", "store_phone", "store_city", "store_state"]
