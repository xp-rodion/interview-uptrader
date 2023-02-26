from django.db import models
from django.urls import reverse


class AbstractMenu(models.Model):
    date_created = models.DateTimeField(verbose_name='Date created', auto_now_add=True)
    slug = models.SlugField(max_length=128, unique=True, verbose_name='Name slug')

    class Meta:
        abstract = True


class Menu(AbstractMenu):
    title = models.CharField(max_length=32, verbose_name='Title Menu')

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return f'{self.title}'


class ItemMenu(AbstractMenu):
    title = models.CharField(max_length=32, verbose_name='Title ItemMenu')
    menu = models.ForeignKey(to=Menu, verbose_name='Parent Menu', on_delete=models.PROTECT, related_name='item_menu', blank=True, null=True)
    parent = models.ForeignKey('ItemMenu', verbose_name='Parent ItemMenu', on_delete=models.PROTECT, default=None, blank=True, null=True, related_name='item_parent')

    class Meta:
        verbose_name = 'ItemMenu'
        verbose_name_plural = 'ItemMenu'

    def __str__(self):
        return f'{self.title}'

    def get_url(self):
        return self.slug
