from django.urls import path

from apps.documentos import views

app_name = 'documento'

urlpatterns = [
    path('create/<int:id>', views.create, name='create'),
    path('list/<int:id>', views.list, name='list'),
    # path('delete', views.delete, name='delete'),
]
