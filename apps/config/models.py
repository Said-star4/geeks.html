from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название",blank=True, null=True)
    description = models.TextField(verbose_name="Описание",blank=True, null=True)
    logo = models.ImageField(upload_to="settings/logo", verbose_name="логотип",blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон",blank=True, null=True)
    email = models.EmailField(verbose_name="Email",blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Адрес",blank=True, null=True)

    instagram = models.URLField(verbose_name="Instagram", blank=True, null=True)
    telegram = models.URLField(verbose_name="Telegram", blank=True, null=True)
    whatsapp = models.URLField(verbose_name="WhatsApp", blank=True, null=True)
    youtube = models.URLField(verbose_name="YouTube", blank=True, null=True)


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название услуги",blank=True, null=True)
    description = models.TextField(verbose_name="Описание",blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена",blank=True, null=True)
    image = models.ImageField(upload_to="services/", verbose_name="Изображение",blank=True, null=True)

