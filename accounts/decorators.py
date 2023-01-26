from django.http import HttpResponse
from django.shortcuts import redirect

## A decorator is a function that takes argument as another function and does some functionality and returns the main function.
def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0]
                if group in allowed_roles:
                    return view_func(request,*args,**kwargs)
                else:
                    return HttpResponse('You are not allowed to view this page')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group=None
        if request.user.group.exists():
            group=request.user.group.all()[0]
        if group=='customer':
            return redirect('user-page')
        elif group=='admin':
            return view_func(request,*args,**kwargs)
    return wrapper_func