from django.db import models

class CategoryProduct(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False,unique=True)


class Product(models.Model):
    code = models.CharField(max_length=4,null=False,blank=False,unique=True)
    onhand_qty = models.FloatField()
    category_id = models.ForeignKey('CategoryProduct',on_delete=models.PROTECT)


class Livestock(models.Model):
    code = models.CharField(max_length=10,null=False,blank=False,unique=True)
    name = models.CharField(max_length=50)
    weight_initial = models.FloatField()
    weight_current = models.FloatField()


class Income(models.Model):
    datetime_in = models.DateTimeField()
    product_id = models.ForeignKey('Product',on_delete=models.PROTECT)
    quantity = models.FloatField()


class Outcome(models.Model):
    datetime_out = models.DateTimeField()
    product_id = models.ForeignKey('Product',on_delete=models.PROTECT)
    quantity = models.FloatField()


class LivestockWeightHistory(models.Model):
    date_record = models.DateField()
    livestock_id = models.ForeignKey('LiveStock',on_delete=models.PROTECT)
    weight = models.FloatField()


