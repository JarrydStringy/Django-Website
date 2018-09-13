from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rentals import views

urlpatterns = [
	#Home Page
    url(r'^$', views.home, name='home'),	# '^$' is for / which is the first page
    #Admin
    url(r'^admin/', admin.site.urls),
    #Individual customer
    url(r'^customer/(\d+)/', views.customer_detail, name='customer_detail'),	#\d+ is 1 or more digit characters for unique pages
    #Individual order
    url(r'^order/(\d+)/', views.order_detail, name='order_detail'),
    #Individual store
    url(r'^store/(\d+)/', views.store_detail, name='store_detail'),
    #Individual vehicle
    url(r'^vehicle/(\d+)/', views.vehicle_detail, name='vehicle_detail'),
]
