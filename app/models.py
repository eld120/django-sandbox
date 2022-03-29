from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
# Create your models here.

class User(AbstractUser):
    something = models.CharField( max_length=50)
    
    def __str__(self):
        return self.first_name + self.last_name

class Listing(models.Model):
    slug = models.SlugField()
    title = models.CharField( max_length=50)    
    owner = models.ForeignKey("app.User", on_delete=models.CASCADE)

    def __str__(self):
        return "Listing title: " + self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Listing, self).save(*args, **kwargs)
        
        
        

class Watchlist(models.Model):
    listing = models.ForeignKey("app.Listing", on_delete=models.CASCADE)
    owner = models.ForeignKey("app.User", on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return f"User key: {self.owner} Listing Key: {self.listing}"