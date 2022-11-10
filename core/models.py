from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    fk_user = models.ForeignKey(User, models.DO_NOTHING)
    addressID = models.AutoField(primary_key=True)
    addressLine1 = models.CharField(max_length=255)
    addressLine2 = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()

    class Meta:
        ordering = ('addressID',)

    def __str__(self):
        add = str(self.addressID)
        return add