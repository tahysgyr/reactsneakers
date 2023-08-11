from django.db import models

# Create your models here.

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

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'