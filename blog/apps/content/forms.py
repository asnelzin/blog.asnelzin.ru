from django import forms
from taggit.forms import TagField
from blog.apps.content.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'slug', 'date', 'body', 'tags']