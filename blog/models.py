from django.db import models
# Create your models here.


class Category(models.Model):
    tilte = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Produts(models.Model):
   
    category = models.ManyToManyField(Category)
    tilte = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=200)
    imag = models.ImageField(upload_to='images',  blank=True, null=True)
    price_sell =  models.FloatField(default=False)
    time_see = models.TimeField(auto_now=True)
    date_publ= models.DateTimeField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name and self.tilte



        

    


     
         
     
       
     
 
   

    