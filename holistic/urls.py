from django.urls import path, include
from .views import HomeView, PostView, AddPostView, UpdatePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name='update_post'),
]
