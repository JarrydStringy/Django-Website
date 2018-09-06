from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<p>Sweet home Alabama</p>')

def car_detail(request, id):
	return HttpResponse('<p>car_detail view with the id {}</p>'.format(id))