from django.urls import path, include
from .views import HomeView, PostView, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
    path('add_post/', AddPostView.as_view(), name='add_post')
]
