from django.db import models

class Customer(models.Model):
    full_name = models.CharField(
        "ФИО заказчика",
        max_length=200,
        blank=True
        )
    phone_number = models.CharField(
        "Номер телефона",
        max_length=40,
        blank=True
        )
