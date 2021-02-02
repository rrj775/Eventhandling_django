from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, User
import json

def home(request):
    customer = Customer.objects.get(first_name="Rajat")
    print(">>>> %s" % request.user)
    return render(request,'home.html',{'customer': customer})

def products(request):
    return render(request,'products.html')

def customer(request):
    return render(request,'customer.html')

def about(request):
    return render(request,'about.html')

def update(request):
    if request.method != 'POST':
        return HttpResponse(json.dumps({'message': 'Method not allowed.'}), content_type="application/json", status=405)
    print(">>> user: %s" % User.objects.get(email=request.user))
    print(">>> active: %s" % json.loads(request.POST.get("active")))
    try:
        user = User.objects.get(email=request.user)
    except User.DoesNotExist:
        return HttpResponse(json.dumps({'message': 'User not found. Please log in to update status.'}), content_type="application/json", status=404)
    active = json.loads(request.POST.get("active", None))
    if active == None:
        return HttpResponse(json.dumps({'message': 'Activity status not provided.'}), content_type="application/json", status=400)
    user.active = active
    user.save(update_fields=['active'])
    return HttpResponse(json.dumps({'message': 'Activity status successfully changed.'}), content_type="application/json", status=200)
