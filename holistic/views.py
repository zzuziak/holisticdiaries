from holistic.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment, Reply
from .forms import PostForm, EditPostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django import template
# def home(request):
    # return render(request, 'home.html', {})


# HOME
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

def AboutView(request):
    return render(request, 'about.html', {})

def ContactView(request):
    return render(request, 'contact.html', {})


def PostView(request, pk, *args, **kwargs):
    post = get_object_or_404(Post, pk=pk)
    cat_menu = Category.objects.all()
    total_likes = post.total_like_count()
    liked = False
    if post.likes.filter(id=post.id).exists():
        liked = True

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'post_details.html', {
        'total_likes': total_likes,
        'liked': liked,
        'form': form,
        'post': post
        })


class AddPostView(CreateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        return super(AddPostView, self).dispatch(request, *args, **kwargs)

    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        return super(UpdatePostView, self).dispatch(request, *args, **kwargs)

    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        return super(DeletePostView, self).dispatch(request, *args, **kwargs)

    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


#CATEGORIES
class AddCategoryView(CreateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        return super(AddCategoryView, self).dispatch(request, *args, **kwargs)

    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__name__contains=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categories_list.html', {'cat_menu_list': cat_menu_list})

#LIKES
def CreateLikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post', args=[str(pk)]))

# COMMENTS

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.kwargs['pk']})

