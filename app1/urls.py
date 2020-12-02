from django.urls import path
from app1 import views
urlpatterns=[
    path('index/',views.index,name='index'),
    path('add_pers/',views.add_pers,name='add_pers'),
    path('edit_pers/<int:id>/',views.edit_pers,name='edit'),
    
    path('addbook/',views.addbook,name='addbook'),
    path('editecr/<int:id>/',views.editecr,name='editecr'),
     path('delete/',views.deletemvt,name='deletemvt'),

    path('list_ecr/',views.list_ecr,name='list_ecr'),
]