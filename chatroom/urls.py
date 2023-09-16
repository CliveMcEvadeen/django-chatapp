from django.urls import path
from . import views

urlpatterns=[
    # path('chat/', views.chat ),
    path('home/', views.home ),
    path('single/', views.single_chat ),
    # path('group/', views.group_chatroom ),
    # path('delete', views.deleted_chatroom ),
]