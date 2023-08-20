from django.db import models
from accounts.models import User


# Profile model
# -----------------------------------------------------------------------------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    products = models.ManyToManyField(to='products.Product', verbose_name='Продукты', blank=True)

    def __str__(self):
        return f'Профиль: {self.user}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
