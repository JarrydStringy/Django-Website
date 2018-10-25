from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rentals import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.mixins import LoginRequiredMixin

urlpatterns = [
#Public pages
	#Home Page
    url(r'^$', views.home, name='home'),	# '^$' is for / which is the first page

#Admin for modifying database from website
    #Admin
    url(r'^admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # /login, /logout, /password_change,
#Management sites for data viewing
    #Home page
    url(r'^manage/', views.manage_home, name='manage_home'),

    #Vehicles
    url(r'^vehicles/', views.manage_vehicles, name='manage_vehicles'),
    #Individual with ID
    url(r'^vehicle/(\d+)/', views.vehicle_id, name='vehicle_id'),
    #Query
    url(r'^vehicle/query/', views.vehicle_query, name='vehicle_query'),

    #Customers
    url(r'^customers/', views.manage_customers, name='manage_customers'),
    #Individual with ID
    url(r'^customer/(\d+)/', views.customer_id, name='customer_id'),
    #Query
    url(r'^customer/query/', views.customer_query, name='customer_query'),

    #Order
    url(r'^orders/', views.manage_orders, name='manage_orders'),
    #Individual with ID
    url(r'^order/(\d+)/', views.order_id, name='order_id'),
    #Query
    url(r'^order/query/', views.order_query, name='order_query'),

    #Store
    url(r'^stores/', views.manage_stores, name='manage_stores'),
    #Individual with ID
    url(r'^store/(\d+)/', views.store_id, name='store_id'),
    #Query
    url(r'^store/query/', views.store_query, name='store_query'),

    # Analytics
    url(r'^analytics/', views.analytics, name='analytics'),
]

urlpatterns += staticfiles_urlpatterns()
