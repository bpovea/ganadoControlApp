from django.db import models

class CategoryProduct(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False,unique=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    active = models.BooleanField(default=True)
    code = models.CharField(max_length=10,null=False,blank=False,unique=True)
    name = models.CharField(max_length=80)
    onhand_qty = models.FloatField()
    category_id = models.ForeignKey('CategoryProduct',on_delete=models.PROTECT)

    def __str__(self):
        return self.code +' - '+ self.name


class Livestock(models.Model):
    active = models.BooleanField(default=True)
    code = models.CharField(max_length=4,null=False,blank=False,unique=True)
    weight_initial = models.FloatField()
    weight_current = models.FloatField()


class Income(models.Model):
    active = models.BooleanField(default=True)
    datetime_in = models.DateTimeField()
    product_id = models.ForeignKey('Product',on_delete=models.PROTECT)
    quantity = models.FloatField()


class Outcome(models.Model):
    active = models.BooleanField(default=True)
    datetime_out = models.DateTimeField()
    product_id = models.ForeignKey('Product',on_delete=models.PROTECT)
    quantity = models.FloatField()


class LivestockWeightHistory(models.Model):
    active = models.BooleanField(default=True)
    date_record = models.DateField()
    livestock_id = models.ForeignKey('LiveStock',on_delete=models.PROTECT)
    weight = models.FloatField()


