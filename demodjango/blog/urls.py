from django.urls import path
from . import views

app_name = 'blog'  # Thêm app_name nếu bạn muốn sử dụng namespace

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:id>/', views.postDetail, name='postDetail'),
]
