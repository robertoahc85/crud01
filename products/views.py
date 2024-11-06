from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_created(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm() 
    return render(request, 'products/product_form.html',{'form':form})       
#Listar productos      
def product_list(request):
    products  = Product.objects.all()
    return render(request,'products/product_list.html',{'products': products})
#Leer detalle
def product_detail(request,id):
    product = get_object_or_404(Product,pk=id)
    return render(request, 'products/product_detail.html',{'product' : product})

def product_update(request,id):
    product = get_object_or_404(Product,pk=id)
    if request.method == 'POST':
        form= ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request,'products/product_form.html',{'form': form})    

def product_delete(request,id):
    product = get_object_or_404(Product,pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html',{'product' : product})