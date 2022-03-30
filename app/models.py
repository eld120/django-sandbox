from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
    something = models.CharField( max_length=50)
    
    def __str__(self):
        return self.first_name + self.last_name
    
    def get_absolute_url(self):
        return reverse("app:home")
    

class Listing(models.Model):
    slug = models.SlugField()
    title = models.CharField( max_length=50)    
    owner = models.ForeignKey("app.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"Listing title: {self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Listing, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("app:listing_detail", kwargs={'slug': self.slug})
    
        

class Watchlist(models.Model):
    listing = models.ForeignKey("app.Listing", on_delete=models.CASCADE)
    owner = models.ForeignKey("app.User", on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('owner', 'listing')
    
    def __str__(self):
        return f"User key: {self.owner} Listing Key: {self.listing}"
    
    def get_absolute_url(self):
        return reverse("app:watchlist_update", kwargs={'slug': self.slug})