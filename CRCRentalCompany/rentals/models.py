from django.db import models

#add blank=True if not possible - This results in value of 0
#add null=True if may be unknown
#use .TextField() for unrestricted length(description)
class Order(models.Model):
	order_create_date = models.DateField()
	pickup_date = models.DateField()
	return_date = models.DateField()
	customer_id = models.IntegerField()
	car_id = models.IntegerField()
	pickup_store_id = models.IntegerField(null=True)
	return_store_id = models.IntegerField(null=True)

class Store(models.Model):
	store_name = models.CharField(max_length=40)
	store_address = models.CharField(max_length=50)
	store_phone = models.CharField(max_length=30)
	store_city = models.CharField(max_length=40)
	store_state = models.CharField(max_length=40)

class Customer(models.Model):
	customer_name = models.CharField(max_length=30)
	customer_phone = models.CharField(max_length=30)
	customer_address = models.CharField(max_length=50)
	customer_birthday = models.DateField()
	customer_occupation = models.CharField(max_length=30)
	SEX_CHOICES = [("M", 'Male'), ('F', 'Female')]
	customer_gender = models.CharField(choices=SEX_CHOICES, max_length=1)

class Vehicle(models.Model):
	make = models.CharField(max_length=30)
	model = models.CharField(max_length=30)
	series = models.CharField(max_length=30)
	year = models.IntegerField()
	price = models.IntegerField()
	engine = models.CharField(max_length=4)
	fuel_type = models.CharField(max_length=30)
	tank_capacity = models.CharField(max_length=8)
	power = models.CharField(max_length=6)
	seats = models.IntegerField()
	transmission = models.CharField(max_length=7)
	body_type = models.CharField(max_length=20)
	drive_type = models.CharField(max_length=3)
	wheelbase = models.CharField(max_length=7)
