from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('<int:blog_id>/', views.entry, name='entry'),
    path('about_me/', views.about_me, name='about me'),
    path('tech_tips/', views.tech_tips, name='tech tips'),
]
