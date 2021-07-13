from django.urls import path
from learning import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),
    path('blog', views.blog, name='blog'), 

]

