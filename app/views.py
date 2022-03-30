from django.contrib.auth import login
from django.contrib import messages
from django.views import generic
from django.shortcuts import redirect, render

from .forms import ListingForm, UserForm, WatchlistForm
from .models import Listing, Watchlist

# Create your views here.
class ListingListView(generic.ListView):
    model = Listing
    template_name = 'app/home.html'
    context_object_name = 'context'


class ListingCreateView(generic.CreateView):
    form_class = ListingForm
    template_name = 'app/deets.html'
    context_object_name = 'context'

    def form_valid(self, form):
        listing_form = form.save(commit=False)
        listing_form.owner = self.request.user
        listing_form.save()
        return super().form_valid(form)
        

class ListingUpdateView(generic.UpdateView):
    form_class = ListingForm
    template_name = 'app/deets.html'
    
    context_object_name = 'context'
    

class WatchlistCreateView(generic.CreateView):
    form_class = WatchlistForm
    template_name = 'app/deets.html'
    context_object_name = 'context'
    
    def form_valid(self, form):
        watchlist_form = form.save(commit=False)
        watchlist_form.owner = self.request.user
        watchlist_form.save()
        super().form_valid(form)
        return redirect('app:home')
    

class WatchlistUpdateView(generic.UpdateView):
    form_class = WatchlistForm
    template_name = 'app/partials/watchlist_form.html'
    
    context_object_name = 'context'
    def form_valid(self, form):
        watchlist_form = form.save(commit=False)
        watchlist_form.owner = self.request.user
        watchlist_form.save()
        super().form_valid(form)
        return render(self.request, 'app/partials/watchlist_form.html', {
            'watchlist_form' : watchlist_form
        })


class UserCreateView(generic.CreateView):
    form_class = UserForm
    template_name = 'app/deets.html'
    
    def form_valid(self, form):
        super().form_valid(form)
        new_user = form.save()
        login(self.request, new_user)
        
        return redirect('app:home')


class UserLoginView(UserCreateView):
    def form_valid(self, form):
        user = form.save()
        login(user)
        super().form_valid(form)
        return redirect('app:home')


def listing_detail(request, slug):
    listing = Listing.objects.get(slug=slug)
    w = Watchlist.objects.get_or_create(listing=listing, owner=request.user)
    watchlist = w[0]    
    
    watchlist_form = WatchlistForm(request.POST or None,
                                   instance=watchlist,
                                   initial={
                                       'active': watchlist.active
                                   })
    if 'active' in request.POST and watchlist_form.is_valid():
        w = watchlist_form.save(commit=False)
        
        w.listing = listing
        w.owner = request.user
        w.save()
        messages.success(request, "Added to Watchlist")
        return render(request, 'app/partials/watchlist_form.html', {
            'watchlist_form' : watchlist_form,
            'listing' : listing
        })
    
    return render(request, 'app/detail.html', {
        'watchlist_form' : watchlist_form,
        'listing' : listing
    })
    
