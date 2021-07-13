from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<slug:category_slug>/<int:id>/', views.blog_detail, name='blog_detail'),
    path('search', views.search, name='search'),
    path('category/<slug:category_slug>/', views.blog, name= 'blog_by_category'),
    # path('category/<slug:category_slug>/<slug:blog_slug>/', views.blog_detail, name='blog_detail'),
 
]