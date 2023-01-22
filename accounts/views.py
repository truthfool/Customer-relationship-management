from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,template_name='accounts/main.html')

def products(request):
    return render(request,template_name='accounts/products.html')

def customer(request):
    return render(request,template_name='accounts/customer.html')
