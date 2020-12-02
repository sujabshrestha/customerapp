from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm
# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(Status='Delivered').count()
    pending = orders.filter(Status='Pending').count()
    context = {
        'customers':customers,
        'orders':orders,
        'total_customers':total_customers,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending':pending
    }
    return render(request,'accounts/home.html',context)


def products(request):
    products = Products.objects.all()
    context ={
        'products':products,
    }
    return render(request,'accounts/products.html',context)



def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()

    total_orders = orders.count()
    context= {'customer':customer,
    'orders':orders,
    'total_orders':total_orders
    }
    return render(request,'accounts/customer.html',context)    



def createorder(request):
    form = OrderForm()
    if request.method == 'POST':
       form = OrderForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/')
    context ={
        'form':form
    }
    return render(request,'accounts/createorder.html',context)

def updateorder(request , pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance = order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance= order)
    if form.is_valid():
        form.save()
        return redirect('/')
    context ={
        'form':form
    }
    return render(request,'accounts/updateorder.html',context)


def deleteorder(request, pk):
    deleteorder = Order.objects.get(id=pk )
    if request.method == 'POST':
        deleteorder.delete()
        return redirect('/')
    context ={
        'item':deleteorder
    }
    return render(request,'accounts/deleteorder.html',context)
