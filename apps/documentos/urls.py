from django.urls import path

from apps.documentos import views

app_name = 'documento'

urlpatterns = [
    path('create/<int:id>', views.create, name='create'),
    path('view/<int:id>', views.view, name='view'),
    # path('delete', views.delete, name='delete'),
]
