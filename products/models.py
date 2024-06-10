from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slyg = models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='url')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural='Категории'
        ordering=("id",)

    def __str__(self) :
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название товара')
    slyg = models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='url')
    desc = models.TextField(blank=True, null=True, verbose_name='Описание')
    img = models.ImageField(upload_to='products_images',blank=True,null=True,verbose_name='Изображение')
    price=models.DecimalField(default=0.00, max_digits=7, decimal_places=2,verbose_name='Цена')
    descount=models.DecimalField(default=0.00, max_digits=7, decimal_places=2,verbose_name='Скидка в процентах')
    quntity=models.PositiveBigIntegerField(default=0,verbose_name='Количество' )
    category=models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural='Товары'
        ordering=("id",)

    def __str__(self) :
        return f'{self.name} количество - {self.quntity}'
    
    def display_id(self):
        return f"{self.id:05}"
    
    def totalprice(self):
        if self.descount:
            return round(self.price - self.price*self.descount/100 ,2)
        
        return self.price