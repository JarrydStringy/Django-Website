from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import Context, loader
from django.shortcuts import render_to_response

from .models import Order
from .models import Store
from .models import Customer
from .models import Vehicle

#Public Pages
	#Home Page
def home(request):
	return render(request, 'main_home.html')

#Management Pages
    #Home page
def manage_home(request):
	return render(request, 'manage_home.html')

def analytics(request):
	return render(request, 'analytics.html')

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
	#Query set
def vehicle_query(request):
	vehicle = Vehicle.objects.raw('SELECT * FROM rentals_vehicle')
	return render(request, 'query_vehicle.html', {'vehicle': vehicle})

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

	#Orders
def manage_orders(request):
    return render(request, 'manage_orders.html', {'id':id})
    #Individual with ID
def order_id(request, id):
	try:
		order = Order.objects.get(id=id)
	except Order.DoesNotExist:
		raise Http404('Order not found :(')
	return render(request, 'detail_order.html', {'order': order})

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
