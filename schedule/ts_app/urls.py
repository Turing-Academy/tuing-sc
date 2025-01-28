from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'classrooms', views.ClassroomViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'lessons', views.LessonScheduleViewSet)
router.register(r'records', views.RecordLinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]