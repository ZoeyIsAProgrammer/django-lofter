from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="blog-home"), 
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="blog-post"), 
    path("post/new/", views.PostCreateView.as_view(), name="blog-post-create"), 
    path("post/<int:pk>/update", views.PostUpdateView.as_view(), name="blog-post-update"),
    path("post/<int:pk>/delete", views.PostDeleteView.as_view(), name="blog-post-delete"),
    path("user/<str:username>/", views.UserDetailView.as_view(), name="user-detail"), 
    path("post-like/<int:pk>/", views.post_like, name="post-like")
]
