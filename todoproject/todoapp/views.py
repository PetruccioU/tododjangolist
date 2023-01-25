
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import TodoListItem

#def todoappView(request):
#    return render(request, 'todolist.html')

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})
# Create your views here.

def DoneListView(request):
    all_done_items = DoneListItem.objects.all()
    return render(request, 'todolist.html', {'done_items':all_done_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return redirect('home',permanent = True)

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return redirect('home',permanent = True)


def pageNotFond(request,exception):
    return HttpResponseNotFound('<h1> Sorry, there is no such page on the website</h1>')

def archive(request,year):
    if int(year)>2022:
        #raise Http404
        return redirect('home',permanent = True) # if permanent= True- redirect 301, else redirect 302(not permanent)
    return HttpResponse(f'<h1> Year Archive: </h1><p>{year}</p>')

