from django.urls import path


from apps.registro_hora import views

app_name='registro_hora'

urlpatterns = [
    path('create/<int:id>', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
    path('list/<int:id>', views.list, name='list'),
]
