from django.contrib import admin

from.models import Order
from.models import Customer
from.models import Vehicle

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ["orderID", "orderCreateDate", "pickupDate", "pickupStoreNo",
		"pickupStoreName", "pickupStoreAddress", "pickupStorePhone", 
		"pickupStoreCity", "pickupStoreState", "returnDate", "returnStoreName",
		"returnStoreAddress", "returnStorePhone", "returnStoreCity",
		"returnStoreState"]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ["customerID", "customerName", "customerPhone", "customerAddress",
		"customerBirthday", "customerOccupation", "customerGender"]

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
	list_display = ["carID", "make", "model", "series", "seriesYear", "priceNew", 
		"engineSize", "fuelSystem", "tankCapacity", "power", "seatingCapacity",
		"transmission", "bodyType", "drive", "wheelbase"]