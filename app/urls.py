from django.urls import path

from . import views

app_name = 'app'


urlpatterns = [
    path('', views.ListingListView.as_view(), name='home'),
    path("listing/<slug>", views.listing_detail, name="listing_detail" ),
    path('listing-create/', views.ListingCreateView.as_view(), name="listing_create"),
    path('listing-update/', views.ListingUpdateView.as_view(), name="listing_update"),
    path('watchlist-create/', views.WatchlistCreateView.as_view(), name='watchlist_create'),
    path('watchlist-update/<slug:slug>', views.WatchlistUpdateView.as_view(), name='watchlist_update'),        
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    ]