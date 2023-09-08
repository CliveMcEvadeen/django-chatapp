from django.urls import path
from . import views

urlpatterns=[
    path('chat/', views.chat ),
    path('home/', views.home ),
    path('single/', views.single_chatroom ),
    path('group/', views.group_chatroom ),
    path('delete_room/', views.deleted_chatroom ),
]