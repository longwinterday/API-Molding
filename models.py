import re

from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


def phone_validator(phone_number: str) -> bool:
    """Валидатор номера телефона"""
    if re.match(r'^\+?1?\d{9,15}$', phone_number):
        return True
    raise ValidationError(_('Phone must be in digits max 15 length, one "+" is allowed'))


class Manufacturer(models.Model):
    """
    Модель класса Производитель
    """
    title = models.CharField(max_length=150, verbose_name=_('Title'), unique=True)
    city = models.CharField(max_length=150, verbose_name=_('City'))
    address = models.CharField(max_length=1000, verbose_name=_('Address'), blank=True, null=True)
    phone = models.CharField(max_length=15, validators=[phone_validator, ], blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['city']
        verbose_name = _('manufacturer')
        verbose_name_plural = _('manufacturers')


class Molding(models.Model):
    """
    Модель класса Багет
    """
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING, related_name='molding', )
    title = models.CharField(max_length=150, verbose_name=_('Title'))
    code = models.CharField(max_length=150, default=_('No code'), verbose_name=_('Code'))
    color = models.CharField(max_length=150, verbose_name=_('Color'))
    price = models.DecimalField(decimal_places=2, max_digits=10000, verbose_name=_('Price'))

    def __str__(self):
        return f'{self.code}_{self.title}'

    class Meta:
        ordering = ['price']
