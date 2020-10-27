from django.urls import path,include
from . import views 
urlpatterns = [
	path('',views.call),
	path('contact',views.contact,name="contact"),
	path('scan',views.scan,name="scan")
   ]
    
