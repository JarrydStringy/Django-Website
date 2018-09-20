from django.db import models

#add blank=True if not possible - This results in value of 0
#add null=True if may be unknown
#use .TextField() for unrestricted length(description)
class Order(models.Model):
	# rentalId = models.IntegerField()#============================
	orderCreateDate = models.DateField()
	pickupDate = models.DateField()
	returnDate = models.IntegerField()
	customerId = models.IntegerField()
	# customerId = models.ManyToManyField('Customer')#=============
	carId = models.DateField()
	# carId = models.ManyToManyField('Vehicle')#===================
	pickupStoreId = models.IntegerField(null=True)
	# pickupStoreId = models.ManyToManyField('Store')#=============
	returnStoreId = models.IntegerField(null=True)
	# returnStoreId = models.ManyToManyField('Store')#=============

	# orderCreateDate = models.DateField()
	# pickupDate = models.DateField()
	# returnDate = models.DateField()
	# customerId = models.IntegerField()
	# carId = models.DateField()
	# pickupStoreId = models.IntegerField(null=True)
	# returnStoreId = models.IntegerField(null=True)

class Store(models.Model):
	# storeId = models.IntegerField()#=============================
	storeName = models.CharField(max_length=40)
	storeAddress = models.CharField(max_length=50)
	storePhone = models.CharField(max_length=30)
	storeCity = models.CharField(max_length=40)
	storeState = models.CharField(max_length=40)

class Customer(models.Model):
	# customerId = models.IntegerField()#===========================
	customerName = models.CharField(max_length=30)
	customerPhone = models.CharField(max_length=30)
	customerAddress = models.CharField(max_length=50)
	customerBirthday = models.DateField()
	customerOccupation = models.CharField(max_length=30)
	SEX_CHOICES = [("M", 'Male'), ('F', 'Female')]
	customerGender = models.CharField(choices=SEX_CHOICES, max_length=1)

class Vehicle(models.Model):
	# vehicleId = models.IntegerField()#===================================
	make = models.CharField(max_length=30)
	model = models.CharField(max_length=30)
	series = models.CharField(max_length=30)
	year = models.IntegerField()
	price = models.IntegerField()
	engine = models.CharField(max_length=4)
	fuelType = models.CharField(max_length=30)
	tankCapacity = models.CharField(max_length=8)
	power = models.CharField(max_length=6)
	seats = models.IntegerField()
	transmission = models.CharField(max_length=7)
	bodyType = models.CharField(max_length=20)
	driveType = models.CharField(max_length=3)
	wheelbase = models.CharField(max_length=7)