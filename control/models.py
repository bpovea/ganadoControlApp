from django.db import models
from datetime import date

class CategoryProduct(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False,unique=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    active = models.BooleanField(default=True)
    code = models.CharField(max_length=10,null=False,blank=False,unique=True)
    name = models.CharField(max_length=80)
    onhand_qty = models.FloatField(null=False,blank=False)
    category_id = models.ForeignKey('CategoryProduct',on_delete=models.PROTECT,null=False)

    def __str__(self):
        return self.code +' - '+ self.name


class Livestock(models.Model):
    active = models.BooleanField(default=True)
    code = models.CharField(max_length=4,null=False,blank=False,unique=True)
    weight_initial = models.FloatField(null=False,blank=False)
    weight_current = models.FloatField(null=False,blank=False)

    def __str__(self):
        return self.code


class Income(models.Model):
    active = models.BooleanField(default=True)
    datetime_in = models.DateTimeField(null=False)
    product_id = models.ForeignKey('Product',on_delete=models.PROTECT,null=False)
    quantity = models.FloatField(null=False,blank=False)
    commentary = models.CharField(max_length=200)

    def __str__(self):
        return str(self.datetime_in) + ' | ' + self.product_id.name + ' : ' + str(self.quantity)


class Outcome(models.Model):
    active = models.BooleanField(default=True)
    datetime_out = models.DateTimeField(null=False)
    product_id = models.ForeignKey('Product',on_delete=models.PROTECT,null=False)
    quantity = models.FloatField(null=False,blank=False)
    livestock_id = models.ForeignKey('LiveStock',on_delete=models.PROTECT)
    commentary = models.CharField(max_length=200)

    def __str__(self):
        return str(self.datetime_out) + ' | ' + self.product_id.name + ' : ' + str(self.quantity)


class LivestockWeightHistory(models.Model):
    active = models.BooleanField(default=True)
    date_record = models.DateField(default=date.today)
    livestock_id = models.ForeignKey('LiveStock',on_delete=models.PROTECT)
    weight = models.FloatField(null=False,blank=False)

    def __str__(self):
        return self.livestock_id.code+', '+str(self.weight) + ' | ' + str(self.date_record)

