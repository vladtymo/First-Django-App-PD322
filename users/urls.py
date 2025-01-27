from django.urls import path

from users import views

# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'users', UsersViewSet)

urlpatterns = [
    path("", views.index),
    path("catalog/", views.catalog),
    path("create/", views.create),
    path("edit/<int:id>", views.edit),
    path("details/<int:id>", views.details),
    path("delete/<int:id>", views.delete),
    path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))
]