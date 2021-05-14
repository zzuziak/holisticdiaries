from django.urls import path
from .views import HomeView, PostView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, CreateLikeView, AddCommentView, AboutView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView, name='about'),
    path('contact', ContactView, name='contact'),
    path('post/<int:pk>', PostView, name='post'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/update/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('categories_list/', CategoryListView, name='categories_list'),
    path('like/<int:pk>', CreateLikeView, name='like_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
