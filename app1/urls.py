from django.urls import path
from app1 import views
urlpatterns=[
    path('index/',views.index,name='index'),
    path('add_pers/',views.add_pers,name='add_pers'),
    path('edit_pers/<int:id>/',views.edit_pers,name='edit'),
    
    path('index_pers/',views.index_pers,name='index_pers'),
    path('mod_addpers/',views.mod_addpers,name='mod_addpers'),
    path('mod_editpers/<int:id>/',views.mod_editpers,name='mod_editpers'),
    
    path('addbook/',views.addbook,name='addbook'),
    path('editecr/<int:id>/',views.editecr,name='editecr'),
     path('delete/',views.deletemvt,name='deletemvt'),

    path('list_ecr/',views.list_ecr,name='list_ecr'),

    path('list_prod/',views.list_prod,name='list_prod'),
    path('mod_add_prod/',views.mod_add_prod,name='mod_add_prod'),
    path('mod_editprod/<int:id>/',views.mod_editprod,name='mod_editprod'),
    path('mod_delprod/<int:id>/',views.mod_delprod,name='mod_delprod'),

]