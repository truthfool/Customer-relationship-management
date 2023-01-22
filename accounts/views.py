from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,template_name='main.html')

def products(request):
    return render(request,template_name='products.html')

def customer(request):
    return render(request,template_name='customer.html')
