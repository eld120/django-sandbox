from django.contrib.auth.forms import UserCreationForm
from django.forms import models
from .models import Listing, User, Watchlist


class ListingForm(models.ModelForm):
    class Meta:
        model = Listing
        fields = ("title",)


class WatchlistForm(models.ModelForm):
    class Meta:
        model = Watchlist
        fields = ("active",)


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
