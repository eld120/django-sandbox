from django.contrib.auth import login, views
from django.contrib import messages
from django.views import generic
from django.shortcuts import redirect, render

from .forms import ListingForm, UserForm, WatchlistForm
from .models import Listing, Watchlist

# Create your views here.
class ListingListView(generic.ListView):
    model = Listing
    template_name = "app/home.html"
    context_object_name = "context"


class ListingCreateView(generic.CreateView):
    form_class = ListingForm
    template_name = "app/deets.html"
    context_object_name = "context"

    def form_valid(self, form):
        listing_form = form.save(commit=False)
        listing_form.owner = self.request.user
        listing_form.save()
        return super().form_valid(form)


class ListingUpdateView(generic.UpdateView):
    form_class = ListingForm
    template_name = "app/deets.html"

    context_object_name = "context"


# class WatchlistCreateView(generic.CreateView):
#     form_class = WatchlistForm
#     template_name = "app/deets.html"
#     context_object_name = "context"
#     success_url = "app:home"

    # def form_valid(self, form):
    #     watchlist_form = form.save(commit=False)
    #     watchlist_form.owner = self.request.user
    #     watchlist_form.save()
    #     super().form_valid(form)
    #     return redirect("app:home")


# class WatchlistUpdateView(generic.UpdateView):
#     form_class = WatchlistForm
#     template_name = "app/detail.html"
#     context_object_name = "context"

#     success_url = "home"

#     def form_valid(self, form):
#         watchlist_form = form.save(commit=False)
#         watchlist_form.owner = self.request.user
#         watchlist_form.save()
#         super().form_valid(form)
#         print(f"-------------{watchlist_form.active}--------------")
#         return render(
#             self.request,
#             "app/deets.html",
#             {"watchlist_form": watchlist_form, "listing": watchlist_form.listing},
#         )

#     def get_object(self):
#         slug = self.kwargs["slug"]
#         l = Listing.objects.get(slug=slug)

#         return Watchlist.objects.get(listing=l, owner=self.request.user)


class UserCreateView(generic.CreateView):
    form_class = UserForm
    template_name = "app/deets.html"

    def form_valid(self, form):
        super().form_valid(form)
        new_user = form.save()
        login(self.request, new_user)

        return redirect("app:home")


class UserLoginView(views.LoginView):
    template_name = 'app/login.html'


def listing_detail(request, slug):
    listing = Listing.objects.get_or_create(slug=slug)
    if request.user.is_authenticated:
        watchlist = Watchlist.objects.get_or_create(
            listing=listing[0], owner=request.user
        )
    else:
        watchlist = ({"active": False},)

    return render(
        request, "app/detail.html", {"listing": listing[0], "watchlist": watchlist[0]}
    )


def watchlist_partial(request, slug):
    # simplified Watchlist toggle using a link instead of a form
    listing = Listing.objects.get_or_create(slug=slug)
    if request.user.is_authenticated:
        watchlist = Watchlist.objects.get_or_create(owner=request.user, listing=listing[0])
        if watchlist[0].active == True:
            watchlist[0].active = False
        else:
            watchlist[0].active = True
        watchlist[0].save()
    else:
        watchlist = (False,)
    #watchlist[0].active if True else False
    

    return render(
        request,
        "app/partials/watchlist_link.html",
        {"watchlist": watchlist[0], "listing": listing[0]},
    )
