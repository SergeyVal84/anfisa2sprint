from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title 


class Topping(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Значение')

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.title 

class Wrapper(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок',
                             help_text='Уникальное название обёртки, не более 256 символов')


    class Meta:
        verbose_name = 'объект «Обёртка»'
        verbose_name_plural = 'Обертки'


    def __str__(self):
        return self.title 


class IceCream(PublishedModel):
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    output_order = models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField()
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обертка',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping)
    is_on_main = models.BooleanField(default=False, verbose_name='Показывать на главной странице')
    

    class Meta:
        verbose_name = 'Мороженное'
        verbose_name_plural = 'Мороженное'
        ordering = ('output_order', 'title')
        

    def __str__(self):
        return self.title 

