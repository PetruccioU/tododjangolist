# ========================================================
# import:

from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import *
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
# Main Views:

# View with a standard ListView class
class todoView(ListView):
    model = TodoListItem
    template_name = 'todolist.html'
    context_object_name = 'posts'
    #extra_context = {'title': 'Task manager'}     # only for string of int
    def get_context_data(self, *, object_list=None, **kwargs):
        cats = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Task manager'
        context['cat_selected'] = 0
        context['cats'] = cats
        return context

    def get_queryset(self):
        return TodoListItem.objects.filter(is_published=1)
#
#def todoappView(request):
#    all_todo_items = TodoListItem.objects.filter(is_done=0)
#    cats = Category.objects.all()
#    context = {
#        'posts': all_todo_items,
#        'cats': cats,
#        'menu': menu,
#        'title': 'Task manager',
#        'cat_selected': 0,
#    }
#    return render(request, 'todolist.html', context=context)



# Show whole task:
class showPost(DetailView):
    model = TodoListItem
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    #pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        post = get_object_or_404(TodoListItem, slug=self.kwargs['post_slug'])
        cats = Category.objects.all()
        cat_current = Category.objects.get(id=post.cat_id)
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        context['cat_for_title'] = cat_current
        context['cats'] = cats
        return context

#def show_post(request, post_slug):
#    post = get_object_or_404(TodoListItem,slug=post_slug)
#    cats = Category.objects.all()
#    cat_current = Category.objects.get(id=post.cat_id)
#    #task = TodoListItem.objects.filter(id=post_id)
#    context = {
#    'post': post,
#    'menu': menu,
#    'title': post.title,
#    'cat_for_title': cat_current,
#    #'cat_selected': post.cat_id,
#    }
#    return render(request, 'post.html', context=context)
#    #return HttpResponse(f"Отображение статьи с id = {post_id}")


# Show tasks of one category

# View with a standard ListView class
class showcatView(ListView):
    model = TodoListItem
    template_name = 'todolist.html'
    context_object_name = 'posts'
    allow_empty = False
    # extra_context = {'title': 'Task manager'}     # only for string of int
    def get_context_data(self, *, object_list=None, **kwargs):
        cats = Category.objects.all()
        catid = Category.objects.get(slug=self.kwargs['cat_slug'])
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Category - ' + str(context['posts'][0].cat)
        context['cat_selected'] = catid.name
        context['cats'] = cats
        return context

    def get_queryset(self):
        return TodoListItem.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

## View of category as function:
#def show_category(request, cat_slug):
#    catid = Category.objects.get(slug=cat_slug)
#    posts = TodoListItem.objects.filter(cat_id=catid.id)
#    cats = Category.objects.all()
#
#    if posts == None:
#        raise Http404()
#
#    context = {
#        'posts': posts,
#        'cats': cats,
#        'menu': menu,
#        'title': 'Task Manager',
#        'cat_selected': catid.name,
#    }
#    return render(request, 'todolist.html', context=context)


# done lists as function:
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


# add form as CreateView class
class addForm(CreateView):
    form_class = AddPostForm
    template_name = 'add.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        cats = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Add new task'
        context['cats'] = cats
        return context

## add form as function:
#def showFormForNewTask(request):
#    if request.method == 'POST':
#        form = AddPostForm(request.POST,request.FILES)
#        if form.is_valid():
#            form.save() # in case of form disconnected from the model, we call model, and its method: TodoListItem.objects.create(**form.cleaned_data)
#            return redirect('home', permanent=True)
#    else:
#        form = AddPostForm()
#    # To provide user with blank form at first time, and if pass/log is incorrect
#    # return filled form for correction
#    context = {
#        'form': form,
#        'menu': menu,
#        'title': 'Task Manager:',
#    }
#    return render(request, 'add.html', context=context)

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
# functional buttons: slug:post_slug
def deleteTodoView(request, post_slug):
    y = TodoListItem.objects.get(slug=post_slug)
    y.delete()
    return redirect('home',permanent = True)

def getYourTodoDone(request, post_slug):
    y = TodoListItem.objects.get(slug=post_slug)
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

#def categories(request, catid):
#    if request.POST:
#        print(request.POST)
#
#    return HttpResponse(f"<h1>Task by title</h1><p>{ catid }<p1>")


