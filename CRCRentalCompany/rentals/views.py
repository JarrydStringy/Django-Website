from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import Context, loader

from .models import Order
from .models import Store
from .models import Customer
from .models import Vehicle

def home(request):
	# customers = Customer.objects.all()
	# return render(request, 'home.html', {'customers', customers})
	
	return HttpResponse('<p>Sweet home Alabama</p>')
	
	# home_template = loader.get_template("html/CRC-home.html")
	# return HttpResponse(home_template.render())

def customer_detail(request, id):
	try:
		customer = Customer.objects.get(id=id)
	except Customer.DoesNotExist:
		raise Http404('Customer not found :(')
	return render(request, 'customer_detail.html', {'customer':customer})
	
	# return HttpResponse('<p>customer detail view with the id {}</p>'.format(id))

def order_detail(request, id):
	try:
		order = Order.objects.get(id=id)
	except Order.DoesNotExist:
		raise Http404('Order not found :(')
	return render(request, 'orders.html', {'order':order})

	# return HttpResponse('<p>order detail view with the id {}</p>'.format(id))

def store_detail(request, id):
	try:
		store = Store.objects.get(id=id)
	except Store.DoesNotExist:
		raise Http404('Store not found :(')
	return render(request, 'stores.html', {'store':store})

	# return HttpResponse('<p>store detail view with the id {}</p>'.format(id))

def vehicle_detail(request, id):
	try:
		vehicle = Vehicle.objects.get(id=id)
	except Vehicle.DoesNotExist:
		raise Http404('Vehicle not found :(')
	return render(request, 'vehicle_detail.html', {'vehicle':vehicle})

	# return HttpResponse('<p>vehicle detail view with the id {}</p>'.format(id))
