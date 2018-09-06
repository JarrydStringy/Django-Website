from django.db import models

#add blank=True if not possible - This results in value of 0
#add null=True if may be unknown
#use .TextField() for unrestricted length(description)
class Order(models.Model):
	orderID = models.IntegerField()
	orderCreateDate = models.DateTimeField()
	pickupDate = models.DateField()
	pickupStoreNo = models.IntegerField()
	pickupStoreName = models.CharField(max_length=40)
	pickupStoreAddress = models.CharField(max_length=50)
	pickupStorePhone = models.CharField(max_length=30)
	pickupStoreCity = models.CharField(max_length=30)
	pickupStoreState = models.CharField(max_length=30)
	returnDate = models.DateField()
	returnStoreNo = models.IntegerField()
	returnStoreName = models.CharField(max_length=40)
	returnStoreAddress = models.CharField(max_length=50)
	returnStorePhone = models.CharField(max_length=30)
	returnStoreCity = models.CharField(max_length=30)
	returnStoreState = models.CharField(max_length=30)

class Customer(models.Model):
	SEX_CHOICES = [("M", 'Male'), ('F', 'Female')]
	customerID = models.IntegerField()
	customerName = models.CharField(max_length=30)
	customerPhone = models.IntegerField()
	customerAddress = models.CharField(max_length=50)
	customerBirthday = models.DateField()
	customerOccupation = models.CharField(max_length=30)
	customerGender = models.CharField(choices=SEX_CHOICES, max_length=1)

class Vehicle(models.Model):
	carID = models.IntegerField()
	make = models.CharField(max_length=30)
	model = models.CharField(max_length=30)
	series = models.CharField(max_length=30)
	seriesYear = models.IntegerField()
	priceNew = models.IntegerField()
	engineSize = models.CharField(max_length=4)
	fuelSystem = models.CharField(max_length=30)
	tankCapacity = models.CharField(max_length=8)
	power = models.CharField(max_length=6)
	seatingCapacity = models.IntegerField()
	transmission = models.CharField(max_length=7)
	bodyType = models.CharField(max_length=20)
	drive = models.CharField(max_length=3)
	wheelbase = models.CharField(max_length=7)
