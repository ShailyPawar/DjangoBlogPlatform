from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # The homepage for the blog
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # URL for post details
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # The homepage for the blog
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # URL for post details
]

