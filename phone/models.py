from django.db import models 
#Create your models 

class items(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class itemsDetails(models.Model): 
    color = models.CharField (max_length=50) 
    price = models.FloatField() 
    qty = models.IntegerField() 
    tax = models.FloatField() 
    img =  models.CharField(max_length=150)
    total = models.FloatField()
    date = models.DateTimeField (auto_now_add=True)
    itemsId = models.ForeignKey(items,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.itemsId.name + ' ' + self.color
    
class Cart(models.Model):
    itemsDetailsId = models.ForeignKey(itemsDetails,on_delete=models.CASCADE)
    userId = models.IntegerField(default=0)
    qty = models.IntegerField(default=1)
    total = models.FloatField(default=1)
    price = models.FloatField()
    total = models.FloatField()
    discount = models.FloatField(default=0)
    net = models.FloatField()
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.itemsDetailsId.itemsId.name + ' ' + self.itemsDetailsId.color+ " " + str(self.userId) 