from products.models import Product
from django.db import models
from django.contrib.auth.models import User
from products.models import Product, Brand

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    fk_user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()

    class Meta:
        ordering = ('order_id',)
    
    def __str__(self):
        oid = str(self.order_id)
        return oid

class OrderDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    fk_user = models.ForeignKey(User, related_name='orderdetails', blank=True, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    fk_order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    fk_product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    fk_brand = models.ForeignKey(Brand, related_name = 'items', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    class Meta:
        ordering = ('detail_id',)
    
    def __str__(self):
        did = str(self.detail_id)
        return did

    def get_total_price(self):
        return (self.quantity * self.price)

class Return(models.Model):
    return_id = models.AutoField(primary_key=True)
    fk_user = models.ForeignKey(User, related_name='returns', blank=True, null=True, on_delete=models.CASCADE)
    fk_details = models.ForeignKey(OrderDetail, related_name='details', on_delete= models.CASCADE)
    status = models.CharField(max_length=20)
    return_reason = models.CharField(max_length=100)

    @property
    def product(self):
        return self.fk_details.fk_product

    class Meta:
        ordering = ('return_id',)
    
    def __str__(self):
        rid = str(self.return_id)
        return rid