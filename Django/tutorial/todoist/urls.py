from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todoist import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
