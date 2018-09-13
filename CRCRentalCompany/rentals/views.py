from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def home(request):
	return HttpResponse('<p>Sweet home Alabama</p>')

def car_detail(request, id):
	return HttpResponse('<p>car_detail view with the id {}</p>'.format(id))

# def customers(request):
# 	template = loader.get_template("rentals/customers.html")
#     return HttpResponse(template.render())
