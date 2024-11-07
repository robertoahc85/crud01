from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from products.models import Product
from .forms import OrderForm

# Create your views here.
def order_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}  # Asegúrate de que esto sea un diccionario, no un conjunto
    return render(request, 'orders/order_list.html', context)

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()   
    return render(request, 'orders/order_form.html',{'form':form})     

# list
# Create