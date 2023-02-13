# ========================================================
# import:
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from .utils import *
from django.views.generic.edit import UpdateView


# ========================================================
# List of tasks as a standard ListView and Mixin
class TodoView(DataMixin, ListView):
    model = TodoListItem
    template_name = 'todolist.html'
    context_object_name = 'posts'
    #extra_context = {'title': 'Task manager'}     # only for str of int

    def get_context_data(self, *, object_list=None, **kwargs):
        #cats = Category.objects.all()
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Task manager')
        context['cat_selected'] = 0
        #context['menu'] = menu
        #context['cats'] = cats
        #context['title'] = 'Task manager'
        return {**context, **c_def}

    def get_queryset(self):
        return TodoListItem.objects.filter(is_published=1, is_done=0).select_related('cat')
        #.select_related(key) query by ForeignKey - prefetch_related(key) by ManyToManyKey


# List of tasks as function
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


# ==============================================================================
# Show whole task, as a Mixin + DetailView class:
class ShowPost(DataMixin, DetailView):
    model = TodoListItem
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        #post = get_object_or_404(TodoListItem, slug=self.kwargs['post_slug'])
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        #cat_current = Category.objects.get(id=post.cat_id)
        #context['cat_for_title'] = post.cat
        #context['title'] = post.slug
        #context['post'] = post
        return {**context, **c_def}

    #def get_object(self, queryset=None):
    #    return TodoListItem.objects.filter(slug='post_slug')
    #def get_queryset(self):
    #    return TodoListItem.objects.filter(slug='post_slug')
        #.select_related(key) query by ForeignKey - prefetch_related(key) by ManyToManyKey

# Show whole task, as a DetailView class:
#class ShowPost(DetailView):
#    model = TodoListItem
#    template_name = 'post.html'
#    slug_url_kwarg = 'post_slug'
#    #pk_url_kwarg = 'post_pk'
#    context_object_name = 'post'
#
#    def get_context_data(self, *, object_list=None, **kwargs):
#        post = get_object_or_404(TodoListItem, slug=self.kwargs['post_slug'])
#        cats = Category.objects.all()
#        cat_current = Category.objects.get(id=post.cat_id)
#        context = super().get_context_data(**kwargs)
#        context['menu'] = menu
#        context['title'] = post.slug
#        context['cat_for_title'] = cat_current
#        context['cats'] = cats
#        return context

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


#========================================================================
# Show tasks by categories with Mixin and ListView:
# Show tasks with Mixin:
class ShowCatView(DataMixin, ListView):
    model = TodoListItem
    template_name = 'todolist.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return TodoListItem.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True, is_done=False).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        catid = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['cat_selected'] = catid.id
        context['cat_selected_name'] = catid.name
        c_def = self.get_user_context(title='Category - ' + str(catid.name))    #(title='Category - ' + str(catid.cat), cat_selected = catid.pk)
        return {**context, **c_def}


## View with a standard ListView class
#class showcatView(ListView):
#    model = TodoListItem
#    template_name = 'todolist.html'
#    context_object_name = 'posts'
#    allow_empty = False
#    # extra_context = {'title': 'Task manager'}     # only for string of int
#
#    def get_context_data(self, *, object_list=None, **kwargs):
#        cats = Category.objects.all()
#        catid = Category.objects.get(slug=self.kwargs['cat_slug'])
#        context = super().get_context_data(**kwargs)
#        context['menu'] = menu
#        context['title'] = 'Category - ' + str(context['posts'][0].cat)
#        context['cat_selected'] = catid.name
#        context['cats'] = cats
#        return context
#
#    def get_queryset(self):
#        return TodoListItem.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True, is_done=False)

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


# ==============================================================================
# Done list as class with DataMixin and ViewList
class DoneList(DataMixin, ListView):
    model = TodoListItem
    template_name = 'donelist.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('about')
    login_url = reverse_lazy('about')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Task manager')
        return {**context, **c_def}

    def get_queryset(self):
        return TodoListItem.objects.filter(is_published=1, is_done=1)

## DoneList as function:
#def DoneList(request):
#    all_done_items = TodoListItem.objects.filter(is_done=1)
#    cats = Category.objects.all()
#    if len(all_done_items) == 0:
#        raise Http404()
#    context = {
#        'posts': all_done_items,
#        'cats': cats,
#        'title': 'Task manager',
#        'menu': menu,
#    }
#    return render(request, 'donelist.html',
#    context=context)


# ==============================================================================
# add form as CreateView class
class AddForm(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'add.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Add new task')
        return {**context, **c_def}

    #def get_context_data(self, *, object_list=None, **kwargs):
    #    cats = Category.objects.all()
    #    context = super().get_context_data(**kwargs)
    #    context['menu'] = menu
    #    context['title'] = 'Add new task'
    #    context['cats'] = cats
    #    return context

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


# ========================================================
# Update Task:
class PostUpdateView(DataMixin, UpdateView):
    model = TodoListItem
    form_class = AddPostForm
    success_message = "Facture mise à jour avec succes"
    template_name = 'update_form.html'
    template_name_suffix = 'update_form'

    def get_queryset(self):
        return TodoListItem.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        catid = TodoListItem.objects.get(slug=self.kwargs['slug'])
        context['post'] = catid
        c_def=self.get_user_context(title='Update task')
        return {**context, **c_def}

    #def get_absolute_url(self):
    #def get_object(self, queryset=None):
    #    return TodoListItem.objects.get(slug=self.kwargs("post_slug"))

    #def get_success_url(self):
    #    return reverse_lazy('update', kwargs={'post_slug': self.get_object().id})


# ===================================================================
# Register and Login
class RegisterUser(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Registration')
        return {**context, **c_def}

    def form_valid(self, form):
        user=form.save()
        login(self.request, user)
        return redirect('home')


class LogUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Login')
        return {**context, **c_def}

    def get_success_url(self):
            return reverse_lazy('home')

    def logout_user(request):
        logout(request)
        return redirect('login')

#=====================================================
#  Feedback view


class FeedbackView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Please give a feedback about us:')
        return {**context, **c_def}

    def form_valid(self, form):
        #user=form.save()
        print(form.cleaned_data)
        #login(self.request, user)
        return redirect('home')


#=====================================================
# Search:


class SearchResultsView(DataMixin, ListView):
    model = TodoListItem
    template_name = 'search.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Search')
        return {**context, **c_def}

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = TodoListItem.objects.filter(
            Q(title__icontains=query) #| Q(state__icontains=query)
        )
        return object_list


#======================================================
# Static views:
class AboutForm(DataMixin, ListView):
    template_name = 'about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='About Us')
        return {**context, **c_def}

    def get_queryset(self):
        return TodoListItem.objects.all()


class MotivationForm(DataMixin, ListView):
    template_name = 'motivational.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Get motivated')
        return {**context, **c_def}  # adding one dictionary to another

    def get_queryset(self):
        return TodoListItem.objects.all()

#def about_form(request):
#    context = {
#        'title': 'Task manager',
#        'menu': menu,
#    }
#    return render(request, 'about.html', context=context)
#
#def motivation_form(request):
#    context = {
#        'title': 'Task manager',
#        'menu': menu,
#    }
#    return render(request, 'motivational.html',context=context)


# ========================================================
# functional buttons: slug:post_slug

def delete_todo_view(request, post_slug):
    if request.user.is_authenticated:
        y = TodoListItem.objects.get(slug=post_slug)
        y.delete()
        return redirect('home',permanent = True)
    else:
        return redirect('home', permanent=True)


def get_your_todo_done(request, post_slug):
    if request.user.is_authenticated:
        y = TodoListItem.objects.get(slug=post_slug)
        y.is_done=1
        y.save(update_fields=["is_done"])
        return redirect('home', permanent=True)
    else:
        return redirect('home', permanent=True)


# ========================================================
# Exeption 404, and archive:


def pageNotFound(request,exception):
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


