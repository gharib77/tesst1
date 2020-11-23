from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('add_pers/',views.add_pers,name='add_pers'),
    path('edit_pers/<int:id>/',views.edit_pers,name='edit'),
]