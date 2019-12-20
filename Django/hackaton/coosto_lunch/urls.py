from django.urls import path
from coosto_lunch import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('coosto-lunch/overviews/', views.OverViewList.as_view()),
    path('coosto-lunch/roles/', views.RoleList.as_view()),
    path('coosto-lunch/users/', views.UserList.as_view()),
    path('coosto-lunch/users/<int:pk>/', views.UserDetail.as_view()),
    path('coosto-lunch/specials/', views.SpecialList.as_view()),
    path('coosto-lunch/specials/<int:pk>/', views.SpecialDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
