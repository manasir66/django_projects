from django.urls import path
from . import views 

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    
    #add task url 
    path('task-list/', views.task_list, name="task-list"),

    #add task
    path('task-create/', views.task_create, name="task-create")

]
