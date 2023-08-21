from turtle import title, width
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.






class Category(models.Model):
    title = models.CharField('Наименование', max_length=75)
    time_create = models.DateField('Дата создания',auto_now_add=True, db_index=True)
    time_update = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title 
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering = ['time_create', 'title']

class Product(models.Model):
    title = models.CharField('Наименование', max_length=75)
    content = models.TextField('Описание продукта', null=True, blank=True)
    width = models.CharField('Вес', max_length=10, null=True)
    price = models.FloatField('Цена', null=True, blank=True)
    new_product = models.BooleanField('новинка', default = False)

    time_create = models.DateField('Дата создания',auto_now_add=True, db_index=True)
    time_update = models.DateField(auto_now=True)
    categorys = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField('Изображение', upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title
   
    def save(self, *args, **kwargs):
        if self.pk:  # если продукт уже существует в базе данных
            old_product = Product.objects.get(pk=self.pk)
            if old_product.price != self.price:  # если цена была изменена
                PriceHistory.objects.create(product=self, price=old_product.price)  # сохраняем старую цену в истории
        super().save(*args, **kwargs)
   
    class Meta:
        verbose_name='Продукт'
        verbose_name_plural='Продукты'
        ordering = ['time_create', 'title'] # Сортируем сначала по дате и времени создания продукта, затем по имени


class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price_history')
    price = models.FloatField('Старая цена')
    date = models.DateTimeField('Дата изменения', auto_now_add=True)
    
    def __str__(self):
        return f"Цена {self.price} для {self.product.title} от {self.date.strftime('%d.%m.%Y')}"
    
    class Meta:
        verbose_name = 'История цены'
        verbose_name_plural = 'Истории цен'
        ordering = ['-date']

# Акции
class Promotion(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='promotion')
    description = models.TextField('Описание акции')

    def __str__(self):
        return f"Акция для {self.product.title}"

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'



### Модели до 8 августа 2023 без истории цены
# class Categorys(models.Model):
#     title = models.CharField('Наименование', max_length=75)
#     time_create = models.DateField('Дата создания',auto_now_add=True, db_index=True)
#     time_update = models.DateField(auto_now=True)
    
#     def __str__(self):
#         return self.title 
#     class Meta:
#         verbose_name='Категория'
#         verbose_name_plural='Категории'
#         ordering = ['time_create', 'title']

# class Product(models.Model):
#     title = models.CharField('Наименование', max_length=75)
#     content = models.TextField('Описание продукта', null=True, blank=True)
#     width = models.CharField('Вес', max_length=10, null=True)
#     price = models.FloatField('Цена', null=True, blank=True)
#     time_create = models.DateField('Дата создания',auto_now_add=True, db_index=True)
#     time_update = models.DateField(auto_now=True)
#     categorys = models.ForeignKey(Categorys, on_delete=models.SET_NULL, null=True, blank=True)
   
#     def __str__(self):
#         return self.title + " " + self.width
#     class Meta:
#         verbose_name='Продукт'
#         verbose_name_plural='Продукты'
#         ordering = ['time_create', 'title'] # Сортируем сначала по дате и времени создания продукта, затем по имени

