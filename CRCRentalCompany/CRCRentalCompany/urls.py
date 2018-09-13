from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from rentals import views

urlpatterns = [
    url(r'^$', views.home, name='home'),	# '^$' is for / which is the first page
    url(r'^admin/', admin.site.urls),
    url(r'^cars/(\d+)/', views.car_detail, name='car_detail'),	#\d+ is 1 or more digit characters for unique pages
]
