from django import forms
from .models import *

# Form bound with the Model

class AddPostForm(forms.ModelForm):
    class Meta:
        model= TodoListItem
        fields = ['title', 'content', 'is_published', 'cat']  # if (fields = '__all__') The Form will show all fields, except ones that are filled automatically











# Form apart from Model
#class AddPostForm(forms.Form):
#    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
#    slug = forms.SlugField(max_length=255, label= 'URL', required=False)
#    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
#    is_published = forms.BooleanField(label= 'Publish now', initial=True)
#    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label='No category')



