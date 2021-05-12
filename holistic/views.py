from holistic.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditPostForm
# def home(request):
    # return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostView(DetailView):
    model = Post
    template_name = 'post_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'post_summary', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'
