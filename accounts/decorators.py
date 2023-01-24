from django.http import HttpResponse
from django.shortcuts import redirect

## A decorator is a function that takes argument as another function and does some work and returns the main function.
def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated():
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func