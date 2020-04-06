from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    catrgory=models.CharField(max_length=50,default="")
    sub_category=models.CharField(max_length=50,default="")
    likes = models.ManyToManyField(User,related_name='likes',blank=True)
    price=models.IntegerField(default=0)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="review/images",default="")

    
    def __str__(self):
        return self.product_name




