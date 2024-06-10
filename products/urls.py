from django.urls import path

from products import views

app_name="products"

urlpatterns = [
    path('<slug:category_slyg>/', views.catalog, name='index'),
    path('search/', views.catalog, name='search'),
    path('product/<slug:product_slyg>/', views.product, name='product'),
 
]