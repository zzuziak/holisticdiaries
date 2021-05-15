from django import forms
from .models import Post, Category, Comment

class PostForm(forms.ModelForm):
    def init(self, *args, **kwargs):
        super(PostForm, self).init(*args, **kwargs)

    class Meta:
        model = Post
        fields = ('title', 'header_image', 'category', 'post_summary', 'body', 'published')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the title'}),
            'category': forms.Select(choices=[choice for choice in Category.objects.all().values_list('name', 'name')], attrs={'class': 'form-control'}),
            'post_summary': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'published': forms.CheckboxInput(),
        }

class EditPostForm(forms.ModelForm):
    def init(self, *args, **kwargs):
        super(EditPostForm, self).init(*args, **kwargs)

    class Meta:
        model = Post
        fields = ('title', 'header_image', 'category', 'post_summary', 'body', 'published')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the title'}),
            'post_summary': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=[choice for choice in Category.objects.all().values_list('name', 'name')], attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'published': forms.CheckboxInput(),

        }


class CommentForm(forms.ModelForm):
    def init(self, *args, **kwargs):
        super(CommentForm, self).init(*args, **kwargs)

    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }