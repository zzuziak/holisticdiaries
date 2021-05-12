from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_summary', 'body')
        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_summary': forms.TextArea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'})
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }