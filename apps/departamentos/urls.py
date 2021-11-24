from django.urls import path

from apps.departamentos import views

app_name = 'departamento'

urlpatterns = [
    path('list', views.list, name='list'),
    # path('edit/<int:id>', views.edit, name='edit'),
    # path('delete', views.delete, name='delete'),
    # path('add', views.add, name='add'),
]
