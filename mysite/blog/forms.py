# from django.forms import modelformset_factory
from blog.models import Post, Comment
from django import forms
from django.forms import BaseModelFormSet


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'type', 'code',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)


class RequiredFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


