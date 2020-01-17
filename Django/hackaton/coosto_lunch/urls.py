from django.urls import path, include
from rest_framework.routers import DefaultRouter

from coosto_lunch import views

router = DefaultRouter()
router.register(r'dates', views.DateViewSet)
router.register(r'attendances', views.AttendanceViewSet)
router.register(r'specials', views.SpecialViewSet)
router.register(r'foodwishes', views.FoodwishesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
