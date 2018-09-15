from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import Context, loader

from .models import Order
from .models import Store
from .models import Customer
from .models import Vehicle

#Home page for public
	#Home Page
def home(request):
	# return HttpResponse('<p>Sweet home Alabama</p>')
	return render(request, 'home.html')

#Management sites for data viewing
    #Login Page
def manage_login(request):
	# return HttpResponse('<p>INSERT LOGIN</p>')
	return render(request, 'manage_login')

    #Home page
def manage_home(request):
	return render(request, 'manage_home.html')

    #Vehicles
def manage_vehicles(request):
    return render(request, 'manage_vehicles.html', {'id':id})
    #Individual with ID
def vehicle_id(request, id):
	try:										#Check for id in db
		vehicle = Vehicle.objects.get(id=id)
	except Vehicle.DoesNotExist:				#Show message if not found 
		raise Http404('Vehicle not found :(')
	return render(request, 'detail_vehicle.html', {'vehicle': vehicle})
	# return HttpResponse('<p>insert vehicle details for id: {}</p>', vehicle.id)
 	# return HttpResponse("""<p>Vehicle details: <br/ ><b>id:</b> {}, <br /><b>make:</b> {}, <br /><b>model:</b> {}, <br /><b>series:</b> {},
 	# 		<br /><b>year:</b> {}, <br /><b>price:</b> {}, <br /><b>engine:</b> {}, <br /><b>fuelType:</b> {}, <br /><b>tankCapcity:</b> {},
 	# 		<br /><b>power:</b> {}, <br /><b>seats:</b> {}, <br /><b>transmission:</b> {}, <br /><b>bodyType:</b> {}, <br /><b>driveType:</b> {},
 	# 		<br /><b>wheelbase:</b> {}</p>"""
 	# 		.format(vehicle.id, vehicle.make, vehicle.model, vehicle.series, vehicle.year, vehicle.price, vehicle.engine, vehicle.fuelType, 
 	# 			vehicle.tankCapacity, vehicle.power, vehicle.seats, vehicle.transmission, vehicle.bodyType, vehicle.driveType, vehicle.wheelbase))
# def vehicle_id(request, id):
# 	try:
# 		vehicle = Vehicle.objects.get(id=id)
# 	except Vehicle.DoesNotExist:
# 		raise Http404('Vehicle not found 😞')
# 		def vehicle_id(request, id):
#  	return HttpResponse(str("""<p>Vehicle details: <br/ ><b>id:</b> {}, <br /><b>make:</b> {}, <br /><b>model:</b> {}, <br /><b>series:</b> {},
# 	<br /><b>year:</b> {}, <br /><b>price:</b> {}, <br /><b>engine:</b> {}, <br /><b>fuelType:</b> {}, <br /><b>tankCapcity:</b> {},
# 	<br /><b>power:</b> {}, <br /><b>seats:</b> {}, <br /><b>transmission:</b> {}, <br /><b>bodyType:</b> {}, <br /><b>driveType:</b> {},
# 	<br /><b>wheelbase:</b> {}</p>""")
#  		.format(vehicle.id, vehicle.make, vehicle.model, vehicle.series, vehicle.year, vehicle.price, vehicle.engine, vehicle.fuelType,
#  			vehicle.tankCapacity, vehicle.power, vehicle.seats, vehicle.transmission, vehicle.bodyType, vehicle.driveType, vehicle.wheelbase))
# 	return render(request, 'vehicle_detail.html', {'id':id})


    #Customers
def manage_customers(request):
    return render(request, 'manage_customers.html', {'id':id})
    #Individual with ID
def customer_id(request, id):
	try:
		customer = Customer.objects.get(id=id)
	except Customer.DoesNotExist:
		raise Http404('Customer not found :(')
	return render(request, 'detail_customer.html', {'customer': customer})
	# return HttpResponse('<p>insert customer details for id: {}</p>', customer.id)
 	# return HttpResponse("""<p>Customer details: <br/ ><b>id:</b> {}, <br /><b>name:</b> {}, <br /><b>phone:</b> {}, <br /><b>address:</b> {},
 	# 	<br /><b>birthday:</b> {}, <br /><b>occupation:</b> {}, <br /><b>gender:</b> {}"""
 	# 	.format(customer.id, customer.name, customer.phone, customer.address, customer.birthday, customer.occupation, customer.gender))

	Orders
def manage_orders(request):
    return render(request, 'manage_orders.html', {'id':id})
    #Individual with ID
def order_id(request, id):
	try:
		order = Order.objects.get(id=id)
	except Order.DoesNotExist:
		raise Http404('Order not found :(')
	return render(request, 'detail_order.html', {'order': order})
 	# return HttpResponse('<p>Sweet home Alabama</p>')
 	# return HttpResponse("""<p>Order details: <br/ ><b>id:</b> {}, <br /><b>orderCreateDate:</b> {}, <br /><b>pickupDate:</b> {}, <br /><b>carId:</b> {},
 	#  	<br /><b>customerId:</b> {}, <br /><b>pickupStoreId:</b> {},, <br /><b>returnStoreId:</b> {}, <br /><b>returnDate:</b> {}"""
 	#  	.format(order.id, order.orderCreateDate, order.pickupDate, order.carId, order.customer_id, order.pickupStoreId, order.returnStoreId, order.returnDate))

	#Stores
def manage_stores(request):
    return render(request, 'manage_stores.html', {'id':id})
    #Individual with ID
def store_id(request, id):
	try:
		store = Store.objects.get(id=id)
	except Store.DoesNotExist:
		raise Http404('Store not found :(')
	return render(request, 'detail_store.html', {'store': store})
 	# return HttpResponse('<p>insert store details for id: </p>')
 	# return HttpResponse('<p>Store details: <br/ ><b>')