from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'post_summary', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'post_summary': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_summary', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the title'}),
            'post_summary': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }