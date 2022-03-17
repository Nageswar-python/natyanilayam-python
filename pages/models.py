from django.db import models

from datetime import date, datetime

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")
    def __str__(self):
        return self.email

class Newsletter(models.Model):
    
    email = models.EmailField(max_length=254)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    

    class Meta:
        verbose_name = ("Newsletter")
        verbose_name_plural = ("Newsletters")

    def __str__(self):
        return self.email
    
class Gallery(models.Model):
    title = models.CharField(max_length =128,null=True)
    img = models.ImageField(upload_to="gallery1/")
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    

    class Meta:
        verbose_name = ("Gallery")
        verbose_name_plural = ("Gallery")

    def __str__(self):
        return self.title
    
class Events(models.Model):
    Date = models.IntegerField(null=True)
    Month = models.CharField(max_length = 128,null=True)
    from_time = models.TimeField(null=True)
    to_time = models.TimeField(null=True)
    place = models.CharField(max_length = 128,null=True)
    title = models.CharField(max_length = 128,null=True)
    description = models.TextField(null=True)
    img = models.ImageField(upload_to="event/")
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Event")

    def __str__(self):
        return self.title
    
class Home(models.Model):
     title = models.CharField(max_length =255,null=True)
     main_title = models.CharField(max_length =120,null=True)
     description = models.TextField(null=True)
     image= models.ImageField(upload_to='slider/%y/%m/%d/')
     
     
 
     class Meta:
         verbose_name = ("Home")
         verbose_name_plural = ("Home")
 
     def __str__(self):
         return self.title