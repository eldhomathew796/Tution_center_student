from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    category_name = models.CharField(max_length=225)
    
    


#class Image(models.Model):
    #photo = models.ImageField(upload_to="image/",null=True)
    #category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    #user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    

class Notes(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to="image/",null=True)
    subject = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    


class Cart(models.Model):
    photo = models.ImageField(upload_to="image/",null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    note = models.ForeignKey(Notes,on_delete=models.CASCADE,null=True)

class Tutor(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/',null=True,blank=True)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    





