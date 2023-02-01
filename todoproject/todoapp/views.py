# ========================================================
# import:

from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import TodoListItem, Category
from .forms import *

# ========================================================
# menu:

menu = [{'title': "All Tasks", 'url_name': 'home'},
        {'title': "Done", 'url_name': 'donelist'},
        {'title': "Add Task", 'url_name': 'add'},
        {'title': "Motivational Quotes", 'url_name': 'motivation'},
        {'title': "About Us", 'url_name': 'about'}
]

# ========================================================
# view pages on navbar:
def todoappView(request):
    all_todo_items = TodoListItem.objects.filter(is_done=0)
    cats = Category.objects.all()
    context = {
        'posts': all_todo_items,
        'cats': cats,
        'menu': menu,
        'title': 'Task manager',
        'cat_selected': 0,
    }
    return render(request, 'todolist.html', context=context)

def show_post(request, post_id):
    task = TodoListItem.objects.filter(id=post_id)
    cats = Category.objects.all()
    context = {
    'posts': task,
    'cats': cats,
    'menu': menu,
    'title': 'Task manager',
    'cat_selected': 0,
    }
    return render(request, 'post.html', context=context)
    #return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request, cat_id):
    posts = TodoListItem.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    cat_current = Category.objects.get(id=cat_id)
    #title_cat = cat_current.name

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Task Manager',
        'cat_selected': cat_id,
        'cat_for_title': cat_current,
    }
    return render(request, 'todolist.html', context=context)

def DoneList(request):
    all_done_items = TodoListItem.objects.filter(is_done=1)
    cats = Category.objects.all()
    if len(all_done_items) == 0:
        raise Http404()
    context = {
        'posts': all_done_items,
        'cats': cats,
        'title': 'Task manager',
        'menu': menu,
    }
    return render(request, 'donelist.html',
    context=context)

def showFormForNewTask(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                TodoListItem.objects.create(**form.cleaned_data)
                return redirect('home', permanent=True)
            except:
                form.add_error(None,'Add error!')
    else:
        form = AddPostForm()

    # To provide user with blank form at first time, and if pass/log is incorrect
    # return filled form for correction

    context = {
        'form': form,
        'menu': menu,
        'title': 'Task Manager:',
    }
    return render(request, 'add.html', context=context)

#def addTodoView(request):
    #x = request.POST['title']
    #y = request.POST['content']
    #new_item = TodoListItem(title = x, content = y)
    #new_item.save()
    #return redirect('home', permanent = True)






#==================================================
# Static views
def AboutForm(request):
    context = {
        'title': 'Task manager',
        'menu': menu,
    }
    return render(request, 'about.html', context=context)

def MotivationForm(request):
    context = {
        'title': 'Task manager',
        'menu': menu,
    }
    return render(request, 'motivational.html',context=context)




# ========================================================
# functional buttons:
def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return redirect('home',permanent = True)

def getYourTodoDone(request, i):
    y = TodoListItem.objects.get(id=i)
    y.is_done=1
    y.save(update_fields=["is_done"])
    return redirect('home', permanent=True)


# ========================================================
# pages as Categories on the Left Sidebar:

##########################################################

# ========================================================
# Exeption 404, and archive:

def pageNotFond(request,exception):
    return HttpResponseNotFound('<h1> Sorry, there is no such page on the website</h1>')

def archive(request,year):
    if int(year)>2022:
        #raise Http404
        return redirect('home',permanent = True) # if permanent= True- redirect 301, else redirect 302(not permanent)
    return HttpResponse(f'<h1> Year Archive: </h1><p>{year}</p>')

def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Task by title</h1><p>{ catid }<p1>")


