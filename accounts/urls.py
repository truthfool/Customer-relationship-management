from django.urls import path
import views

urlpatterns=[
    path('',views.home,name='home'),
    path('',views.products,name='products'),
    path('',views.customer,name='customer'),
]