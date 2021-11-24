from django.urls import path


from apps.funcionarios import views

app_name = 'funcionario'

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
    path('add', views.add, name='add'),
]
