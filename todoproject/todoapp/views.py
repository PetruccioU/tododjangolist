

from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import TodoListItem, Category

def todoappView(request):
    all_todo_items = TodoListItem.objects.filter(is_done=0)
    #for i in TodoListItem.objects.filter(is_done=0):
    #    ids = i.cat_id
    #    show_cats = Category.objects.filter(id=ids)
    return render(request, 'todolist.html',
    {'all_items':all_todo_items}) #,'cat':show_cats
# Create your views here.

def DoneList(request):
    all_done_items = TodoListItem.objects.filter(is_done=1)
    show_cats = Category.objects.all
    return render(request, 'donelist.html',
    {'all_done': all_done_items,'cat':show_cats})

def addTodoView(request):
    x = request.POST['title']
    y = request.POST['content']
    new_item = TodoListItem(title = x, content = y)
    new_item.save()
    return redirect('home', permanent = True)

def showFormForNewTask(request):
    return render(request, 'add.html')

def AboutForm(request):
    return render(request, 'about.html')

def MotivationForm(request):
    return render(request, 'motivational.html')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return redirect('home',permanent = True)

def getYourTodoDone(request, i):
    y = TodoListItem.objects.get(id=i)
    y.is_done=1
    y.save(update_fields=["is_done"])
    return redirect('home', permanent=True)


def pageNotFond(request,exception):
    return HttpResponseNotFound('<h1> Sorry, there is no such page on the website</h1>')

def archive(request,year):
    if int(year)>2022:
        #raise Http404
        return redirect('home',permanent = True) # if permanent= True- redirect 301, else redirect 302(not permanent)
    return HttpResponse(f'<h1> Year Archive: </h1><p>{year}</p>')

def Technical_problem(request):
    all_todo_items = TodoListItem.objects.filter(is_done=0,cat_id=1)
    return render(request, 'Technical problem.html',
                  {'all_items': all_todo_items})  # ,'cat':show_cats

def Management_task(request):
    all_todo_items = TodoListItem.objects.filter(is_done=0, cat_id=2)
    return render(request, 'Management task.html',
                  {'all_items': all_todo_items})  # ,'cat':show_cats

def Marketing_task(request):
    all_todo_items = TodoListItem.objects.filter(is_done=0, cat_id=3)
    return render(request, 'Marketing task.html',
                  {'all_items': all_todo_items})  # ,'cat':show_cats

def HR_task(request):
    all_todo_items = TodoListItem.objects.filter(is_done=0, cat_id=4)
    return render(request, 'HR task.html',
                  {'all_items': all_todo_items})  # ,'cat':show_cats

def Analysis_task(request):
    all_todo_items = TodoListItem.objects.filter(is_done=0, cat_id=5)
    return render(request, 'Analysis task.html',
                  {'all_items': all_todo_items})  # ,'cat':show_cats

def Self_motivation_task(request):
    all_todo_items = TodoListItem.objects.filter(is_done=0, cat_id=6)
    return render(request, 'Self-motivation task.html',
                  {'all_items': all_todo_items})  # ,'cat':show_cats







