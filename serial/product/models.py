from django.db import models

# Create your models here.
class product(models.Model):
    productName=models.CharField(max_length=20,primary_key=True)
    price=models.IntegerField(null=True)
    description=models.CharField(max_length=20)
     
    def __str__(self):
        return self.productName