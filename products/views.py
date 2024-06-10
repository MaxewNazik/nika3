from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404,get_list_or_404, render

from products.models import Products
from products.utils import q_search

def catalog(request, category_slyg=None):

    page=request.GET.get('page', 1)
    on_sale=request.GET.get('on_sale', None)
    order_by=request.GET.get('order_by', None)
    query=request.GET.get('q', None)
    
    if category_slyg=="vse-tovary":
        products=Products.objects.all()
    elif query:
        products=q_search(query)
    else:
        products= get_list_or_404(Products.objects.filter(category__slyg=category_slyg))
    
    if on_sale:
        products=products.filter(descount__gt=0)
    if order_by and order_by != "default":
        products=products.order_by(order_by)

    paginator= Paginator(products, 3)   
    cur_page = paginator.page(int(page))

    context = {
        "title": "Каталог",
        "products": cur_page,
        "slug_url": category_slyg,
    }
    return render(request, "products/catalog.html", context)


def product(request, product_slyg):


    product=Products.objects.get(slyg=product_slyg)

    context={
        'product':product
    }
    
    return render(request, "products/product.html", context=context)
