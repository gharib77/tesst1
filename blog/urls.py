from django.urls import path
from blog import views
urlpatterns=[
    path('',views.blog_index,name='blog_index'),
    path('article/<str:name>/',views.article,name='articl')
]