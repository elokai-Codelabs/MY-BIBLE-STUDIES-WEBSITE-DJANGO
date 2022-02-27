from django.urls import path    
from . import views

app_name = "app"

urlpatterns=[
    path('',views.index,name='index'),
    path('projects/',views.projects,name='projects'),
    path('project/<str:pk>/',views.project,name='single-project'),
    path('bible/',views.bible,name='bible'),
    path('videos/',views.videos,name='videos'),
    path('send-email/',views.send_email,name='send_email'),
    path('create-project/',views.createProject,name='create_project'),
]