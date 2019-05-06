from django.urls import path
from blog import views
from blog.views import (
        PostListView,
        PostDetailView,
        PostCreateView,
        PostUpdateView,
        PostDeleteView,
        UserPostListView,
    )

app_name = "blog"

urlpatterns = [
    path('', PostListView.as_view(), name = "home"),
    path('user/<str:username>', UserPostListView.as_view(), name = "author_post"),
    path('blog/<int:pk>', PostDetailView.as_view(), name = "detail"),
    path('blog/<int:pk>/update', PostUpdateView.as_view(), name = "update"),
    path('blog/<int:pk>/delete', PostDeleteView.as_view(), name = "delete"),
    path('blog/create', PostCreateView.as_view(), name = "create"),
    path('about/', views.about, name = "about"),
]
