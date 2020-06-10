from django.urls import path
from User_App import views

urlpatterns = [
    path('', views.index, name = "Index and Add page"),
    path('delete/<id>', views.delete, name = "Delete"),
    path('edit/<id>', views.edit, name = "Edit"),
    path('update/<id>', views.update, name = 'Update'),
]