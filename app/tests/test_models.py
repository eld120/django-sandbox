from django.test import TestCase

from ..models import User, Listing, Watchlist


# Create your tests here.
class TestStuff(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            id=1,
            username='eldarin',
            first_name='seya',
            last_name='afazi',
            password='dontuse',
            email='devteam@origma.io',
            is_active=True,
            something='some shit'
        )
        self.listing = Listing.objects.create(
            id=1,
            title = 'some title here',
            owner =  self.user
        )
        self.watchlist = Watchlist.objects.create(
            id=1,
            listing = self.listing,
            owner = self.user
        )
        self.listing2 = Listing.objects.create(
            id=2,
            title = 'second interesting title',
            owner = self.user
        )
    def tearDown(self):
        del self.user
        del self.listing
        del self.watchlist
        del self.listing2
        
    
    def test_watchlist_owner(self):
        assert self.watchlist.owner == self.user
        
    def test_watchlist_new_owner(self):
        watchlist2 = Watchlist.objects.create(owner = self.user, listing = self.listing2)
        assert watchlist2.owner == self.user
        assert watchlist2.listing == self.listing2