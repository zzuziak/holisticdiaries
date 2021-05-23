from django.urls import path
from .views import HomeView, PostView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, MarkNotifAsRead, CreateLikeView, AddCommentView, AboutView, ContactView, TagView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView, name='about'),
    path('contact', ContactView, name='contact'),
    path('post/<slug:slug>', PostView, name='post'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/update/<slug:slug>', UpdatePostView.as_view(), name='update_post'),
    path('post/delete/<slug:slug>', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('tag/<str:tag>/', TagView, name='tag'),
    path('categories_list/', CategoryListView, name='categories_list'),
    path('like/<int:pk>', CreateLikeView, name='like_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('post/<int:pk>/notif/', MarkNotifAsRead, name='read_notif'),
]
