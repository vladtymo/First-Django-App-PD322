from django.urls import path

from users import views

urlpatterns = [
    path("", views.index),
    path("catalog/", views.catalog),
    path("create/", views.create),
    path("edit/<int:id>", views.edit),
    path("details/<int:id>", views.details),
    path("delete/<int:id>", views.delete),
]
