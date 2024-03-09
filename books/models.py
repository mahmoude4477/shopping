from django.db import models

# Create your models here.


class books(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    qty = models.IntegerField(default=1) 
    def __str__(self):
        return self.name
class Cart(models.Model):
    bookId = models.ForeignKey(books, on_delete=models.CASCADE)
    userId = models.IntegerField(default=0)
    def __str__(self):
        return self.bookId.name
    
class doneBuy(models.Model):
    bookId = models.ForeignKey(books, on_delete=models.CASCADE)
    userId = models.IntegerField(default=0)
    def __str__(self):
        return self.bookId.name
    
    

        