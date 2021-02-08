from django.urls import include, path 

from . import views

urlpatterns = [
    path("reminder-list-all/", views.list_reminders, name="reminder-list-all"),

    path("reminder-list-one/<str:pk>/", views.list_one, name="reminder-list-one"),
    
    path("reminder-add/", views.add_reminder, name="reminder-add"),
    
    path("reminder-update/<str:pk>/", views.update_reminder, name="reminder-update"),
    
    path("reminder-delete/<str:pk>/", views.delete_reminder, name="reminder-delete")
]
