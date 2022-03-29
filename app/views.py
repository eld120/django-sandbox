from django.views import generic
from django.shortcuts import render

from .models import Listing, User, Watchlist

# Create your views here.
class ListingListView(generic.ListView):
    model = Listing


class ListingCreateView(generic.CreateView):
    model = Listing
    template_name = ''
    fields = ['title']


class ListingUpdateView(generic.UpdateView):
    model = Listing
    template_name = ''
    fields = ['title']


class WatchlistCreateView(generic.CreateView):
    model = Watchlist
    template_name = ''
    fields = ['active']
    

class WatchlistUpdateView(generic.UpdateView):
    model = Watchlist
    template_name = ''
    fields = ['active']


def listing_detail(request, slug):
    return render(request, )
    
