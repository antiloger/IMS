from django.urls import path

from . import views

urlpatterns = [
    path("<str:model_name>", views.index, name="index"),
    path('add/', views.add, name='add'),
    path("update/<str:model_name>/<int:std_ID>", views.update , name='update'),
]

