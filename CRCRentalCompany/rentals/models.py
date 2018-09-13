from django.db import models

#add blank=True if not possible - This results in value of 0
#add null=True if may be unknown
#use .TextField() for unrestricted length(description)
class Order(models.Model):
	orderCreateDate = models.DateField()
	pickupDate = models.DateField()
	returnDate = models.IntegerField()
	customerId = models.IntegerField()
	carId = models.DateField()
	pickupStoreId = models.IntegerField(null=True)
	returnStoreId = models.IntegerField(null=True)

class Store(models.Model):
	storeName = models.CharField(max_length=40)



class Customer(models.Model):
	customerName = models.CharField(max_length=30)
	customerPhone = models.IntegerField()
	customerAddress = models.CharField(max_length=50)
	customerBirthday = models.DateField()
	customerOccupation = models.CharField(max_length=30)
	SEX_CHOICES = [("M", 'Male'), ('F', 'Female')]
	customerGender = models.CharField(choices=SEX_CHOICES, max_length=1)

class Vehicle(models.Model):
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


#
