from django.shortcuts import render, redirect
from django.contrib import messages
from.models import Product

# Create your views here.


def product_create(request):
    if request.method == "POST":
        name            = request.POST['name']
        purchase_price  = float(request.POST['purchase_price'])
        selling_price   = float(request.POST['selling_price'])
        quantity        = int(request.POST['quantity'])

        item_product = Product(name = name , purchase_price = purchase_price, selling_price = selling_price ,quantity = quantity)
        item_product.save()

        messages.success(request,'Sản phẩm đã được tạo thành công !')

        return redirect('/')

    
    
    
    return render(request, 'product_create.html', {})




def product_list(request):
    items_product = Product.objects.all()

    return render(request, 'product_list.html', {
        "items_product" : items_product
        })





def product_update(request , product_id):
    item_product = Product.objects.get(id=product_id)
    
    
    if request.method == "POST":
        name            = request.POST['name']
        purchase_price  = float(request.POST['purchase_price'])
        selling_price   = float(request.POST['selling_price'])
        quantity        = int(request.POST['quantity'])
        sold_quantity      = int(request.POST['sold_quantity'])

        item_product.name = name
        item_product.purchase_price = purchase_price
        item_product.selling_price = selling_price
        item_product.quantity = quantity
        item_product.sold_quantity = sold_quantity

        
        item_product.save()

        messages.success(request,'Sản phẩm đã được cập nhật thành công !')

        return redirect('/')


    return render(request, 'product_update.html', {"item_product" : item_product}) 



def product_delete(request , product_id):
    item_product = Product.objects.get(id=product_id)
    item_product.delete() 

    messages.success(request,'Sản phẩm đã được xóa thành công !')

    return redirect('/')