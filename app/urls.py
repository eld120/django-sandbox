from django.urls import path

from . import views

app_name = 'app'


urlpatterns = [
    path('', views.ListingListView.as_view(), name='home'),
    path("listing/<slug>", views.listing_detail, name="listing-detail" ),
    path('listing-create/', views.ListingCreateView.as_view(), name="listing-create"),
    path('listing-update/', views.ListingUpdateView.as_view(), name="listing-update"),
    path('watchlist-create/', views.WatchlistCreateView.as_view(), name='watchlist-create'),
    path('watchlist-update/', views.WatchlistUpdateView.as_view(), name='watchlist-update')           
    ]