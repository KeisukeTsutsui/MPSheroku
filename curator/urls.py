from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [
    # path('',views.index, name = 'index'),
    # url(r'',HelloView.as_view(),name='index'),
    path('',views.curator, name='curator'),
    path('showTable',views.showTable, name='showTable'),
    path('showImage',views.showImage, name='showImage'),
    path('showUser',views.showUser, name='showUser'),
    path('showPainting',views.showPainting, name='showPainting'),
    path('editTable',views.editTable, name='editTable'),
    path('editImage',views.editImage, name='editImage'),
    path('editUser',views.editUser, name='editUser'),
    path('editPainting',views.editPainting, name='editPainting'),
    path('storeImage',views.storeImage, name='storeImage'),
    path('searchView',SearchView.as_view(), name='searchView'),
] 