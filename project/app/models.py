from django.db import models
from django.contrib.auth import get_user_model
<<<<<<< HEAD

=======
>>>>>>> 22fde60a6e69883344a0e6115f03b0ccac886a50
# Create your models here.

User = get_user_model()

class Images(models.Model):
    images = models.ImageField('Изображения', upload_to='products/pictures/')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

class Products(models.Model):
    image = models.ImageField('Изображение', upload_to='products/pictures', null=True)
    name = models.CharField('Название', max_length=30, null=True)
    brand = models.CharField('Производитель', max_length=16, null=True)
    price = models.IntegerField('Цена', null=True)
    preview = models.ImageField('Изображения для предпросмотра', upload_to='products/preview/', null=True)
    import_img = models.ManyToManyField('Images', blank=True, null=True)
    specifications = models.CharField('Характеристики', null=True, max_length=1800)
    description = models.CharField('Описание', null=True, max_length=500)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

<<<<<<< HEAD
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quanity = models.PositiveIntegerField(default=1)
    price_sale = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)

    class Meta:
        verbose_name = 'Корзина'
        ordering = ['-id']
=======

class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quanity = models.PositiveIntegerField(default=1)
    price_sale = models.DecimalField(max_digits=10,decimal_places=2,default=0,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0,null=True)

    class Meta:
        verbose_name = 'Корзина'
        ordering =['-id']
>>>>>>> 22fde60a6e69883344a0e6115f03b0ccac886a50
