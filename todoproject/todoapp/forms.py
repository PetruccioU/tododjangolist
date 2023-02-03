from django import forms
from django.core.exceptions import ValidationError

from .models import *

# Form bound with the Model

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Category is not selected'
        self.fields['photo'].required = False

    class Meta:
        model= TodoListItem
        fields = ['title', 'slug', 'content', 'photo', 'is_done', 'is_published', 'cat']  # if (fields = '__all__') The Form will show all fields, except ones that are filled automatically
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),

        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 30:
            raise ValidationError('Title length is over 30 symbols!')

        return title






# Form apart from Model
#class AddPostForm(forms.Form):
#    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
#    slug = forms.SlugField(max_length=255, label= 'URL', required=False)
#    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
#    is_published = forms.BooleanField(label= 'Publish now', initial=True)
#    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label='No category')



