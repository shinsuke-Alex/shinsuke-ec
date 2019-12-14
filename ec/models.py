from django.db import models

class Ec(models.Model):
    name = models.CharField("カテゴリー名", max_length=32)

class Product(models.Model):
    ec = models.ForeignKey(Ec, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField("商品名", max_length=128)
    price = models.PositiveIntegerField("価格")