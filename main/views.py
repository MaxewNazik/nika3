from django.shortcuts import render
from django.shortcuts import render

from products.models import Categories
# Create your views here.
def index(request):

    

    context = {
        'title': 'Home - Главная страницу',
        'content': 'Магазин керамической плитки и керамического гранита Ника',
        
    } 


    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title':'Home - Информация о нас',
        'content' :'О нас',
        'text_on_page':'Ника - это магазин по продаже керамической плитки и керамического гранита'

    }
    return render (request,'main/about.html', context)