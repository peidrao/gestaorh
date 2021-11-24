from django.urls import path


from apps.empresas import views

app_name='empresa'

urlpatterns = [
    path('create', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
]
