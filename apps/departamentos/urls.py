from django.urls import path

from apps.departamentos import views

app_name = 'departamento'

urlpatterns = [
    path('list', views.list, name='list'),
    path('create', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete', views.delete, name='delete'),
]
