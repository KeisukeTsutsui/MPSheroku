from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [
    # path('',views.index, name = 'index'),
    # url(r'',HelloView.as_view(),name='index'),
    path('',views.DBView, name='dbView'),
    path('user',views.user, name='user'),
    path('image',views.image, name='image'),
    # path('words',views.words, name='words'),
    path('painting',views.painting, name='painting'),
]