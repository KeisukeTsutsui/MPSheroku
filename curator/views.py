from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.db.models import Q
from .forms import *
from .models import *
from datetime import datetime
#
def curator(request):
    users = User.objects.all()
    images = Image.objects.all()
    paintings = Painting.objects.all()
    params = {
        'title':'Curator',
        'users':users,
        'images':images,
        'paintings':paintings,
    }
    return render(request, 'curator/curator.html',params)

##ShowTable Page
def showTable(request):
    users = User.objects.all()
    images = Image.objects.all()
    paintings = Painting.objects.all()
    params = {
        'title':'ShowTable',
        'users':users,
        'images':images,
        'paintings':paintings,
    }
    return render(request, 'curator/showTable.html',params)

def showUser(request):
    users = User.objects.all()
    params = {
        'title':'user',
        'users':users,
    }
    return render(request, 'curator/showUser.html',params)

def showImage(request):
    images = Image.objects.all()
    params = {
        'title':'image',
        'images':images,
    }
    return render(request, 'curator/showImage.html',params)

def showPainting(request):
    paintings = Painting.objects.all()
    params = {
        'title':'Pinting',
        'paintings':paintings,
    }
    return render(request, 'curator/showPainting.html',params)


##EditTable Page
def editTable(request):
    users = User.objects.all()
    images = Image.objects.all()
    paintings = Painting.objects.all()
    params = {
        'title':'ShowTable',
        'users':users,
        'images':images,
        'paintings':paintings,
    }
    return render(request, 'curator/editTable.html',params)

def editUser(request):
    users = User.objects.all()
    params = {
        'title':'user',
        'users':users,
    }
    return render(request, 'curator/editUser.html',params)

def editImage(request):
    images = Image.objects.all()
    params = {
        'title':'image',
        'images':images,
    }
    return render(request, 'curator/editImage.html',params)

def editPainting(request):
    paintings = Painting.objects.all()
    params = {
        'title':'Pinting',
        'paintings':paintings,
    }
    return render(request, 'curator/editPainting.html',params)

def storeImage(request):
    if (request.method == 'POST'):
        iFile = request.POST['image']
        path = '/static/'+iFile
        images = Image(image=iFile,path=path)
        images.save()
        return redirect(to='/curator')
    params = {
        'title':'storeImage',
        'form':ImageForm()
    }
    return render(request, 'curator/storeImage.html',params)


class SearchView(generic.ListView):
    template_name = 'curator/search.html'
    model = Painting

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        user = User.objects.filter(Q(name=q_word))

        if q_word:
            object_list = Painting.objects.filter(
                Q(user_id=user.get()))
        else:
            object_list = None
        return object_list