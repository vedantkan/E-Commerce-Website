from io import BytesIO
from PIL import Image
from django.db import models
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    slug = models.SlugField()

    class Meta:
        ordering = ('category_name',)
    
    def __str__(self):
        return self.category_name

class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=20)
    fk_user = models.ForeignKey(User, blank = True, null = True, on_delete=models.CASCADE)
    slug = models.SlugField()

    class Meta:
        ordering = ('brand_name',)
    
    def __str__(self):
        return self.brand_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    descrpt = models.CharField(max_length=500)
    quantity = models.IntegerField()
    fk_category = models.ForeignKey(Category, related_name='category', null = True, blank = True, on_delete= models.CASCADE)
    fk_user = models.ForeignKey(User, related_name='products', null = True, blank = True, on_delete=models.CASCADE)
    fk_brand = models.ForeignKey(Brand, null = True, blank = True, on_delete=models.CASCADE)
    price = models.FloatField()
    slug = models.SlugField()
    image = models.ImageField(upload_to = 'uploads/', blank = True, null = True)
    thumbnail = models.ImageField(upload_to = 'uploads/', blank = True, null = True)

    class Meta:
        ordering = ('product_name',)
    
    def __str__(self):
        return self.product_name
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url

            else:
                return 'https://via.placeholder.com/240x240x.jpg'

    def make_thumbnail(self, image, size = (300,300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality = 85)

        thumbnail = File(thumb_io, name = image.name)

        return thumbnail

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    fk_product = models.ForeignKey(Product, related_name='products', on_delete= models.CASCADE)
    review = models.CharField(max_length=500, blank=True, null=True)
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        rid = str(self.review_id)
        return rid