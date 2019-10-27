from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]
