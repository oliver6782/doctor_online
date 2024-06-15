# from django.db import models

# # Create your models here.
# class Station(models.Model):
#     station_id = models.IntegerField()
#     station_name = models.CharField(max_length=50)
#     def __str__(self):
#         return self.station_name
    
# class Category(models.Model):
#     category_id = models.IntegerField()
#     station = models.ForeignKey(Station,on_delete=models.PROTECT)
#     category_name = models.CharField(max_length=50)
#     def __str__(self):
#         return self.category_name
    
# class Item(models.Model):
#     id = models.IntegerField()
#     item_name = models.CharField( max_length=200)
#     stock = models.IntegerField()
#     category = models.ForeignKey(Category,on_delete=models.PROTECT)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     description = models.CharField( max_length=5000)
#     def __str__(self):
#         return self.item_name
    
