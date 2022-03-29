from django.forms import  models
from .models import Listing, Watchlist


class ListingForm(models.ModelForm):
    class Meta:
        model = Listing
        fields = ['title']
    
class WatchlistForm(models.ModelForm):
    class Meta:
        model = Watchlist
        fields = ['active']