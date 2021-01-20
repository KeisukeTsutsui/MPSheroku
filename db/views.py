from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import *
from .models import *
from datetime import datetime


def DBView(request):
    users = User.objects.all()
    images = Image.objects.all()
    paintings = Painting.objects.all()
    params = {
        'title':'DBView',
        'users':users,
        'images':images,
        'paintings':paintings,
        'image':'/static/H07-5_Nisshinkan_iai.jpg',
    }
    return render(request, 'db/dbView.html',params)

def user(request):
    if (request.method == 'POST'):

        obj = User()
        users = UserForm(request.POST, instance=obj)
        users.save()
        return redirect(to='/db')
    params = {
        'title':'db/user.html',
        'form':UserForm()
    }
    return render(request, 'db/user.html',params)

def image(request):
    if (request.method == 'POST'):
        iFile = request.POST['image']
        path = '/static/'+iFile
        images = Image(image=iFile,path=path)
        images.save()
        return redirect(to='/db')
    params = {
        'title':'db/image.html',
        'form':ImageForm()
    }
    return render(request, 'db/image.html',params)

def painting(request):
    if (request.method == 'POST'):
        user_id = User.objects.get(id=request.POST['user_id'])
        title = request.POST['title']
        pFile = request.POST['painting']
        path = '/static/'+pFile
        date = datetime.today().strftime('%Y-%m-%d')
        paintings = Painting(user_id=user_id,title=title,painting=pFile,path=path,date=date)
        paintings.save()
        return redirect(to='/db')
    params = {
        'title':'db/painting.html',
        'form':PaintingForm()
    }
    return render(request, 'db/painting.html',params)

# def words(request):
#     if (request.method == 'POST'):
#         word = request.POST['dialogue']
#         attribute = request.POST['attribute']
#         wordsi = Word(dialogue=word,attribute=attribute)
#         wordsi.save()
#         return redirect(to='/db')
#     params = {
#         'title':'db/words.html',
#         'form':WordForm()
#     }
#     return render(request, 'db/words.html',params)