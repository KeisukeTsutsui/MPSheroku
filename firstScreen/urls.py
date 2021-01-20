from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', CoverPage.as_view(), name = 'coverpage'),
    path('artillery', ArtilleryPage.as_view(), name = 'artillery'),
    path('manner', MannerPage.as_view(), name = 'manner'),
    path('reading', ReadingPage.as_view(), name = 'reading'),
    path('archery', ArcheryPage.as_view(), name = 'archery'),
    path('iai', IaiPage.as_view(), name = 'iai'),
    path('jujutsu', JujutsuPage.as_view(), name = 'jujutsu'),
    path('sojutsu', SojutsuPage.as_view(), name = 'sojutsu'),
    path('riding', RidingPage.as_view(), name = 'riding'),
    path('test_move', TestPage.as_view(), name = 'test_move')
    ##path('',views.cover, name = 'coverpage'),
]