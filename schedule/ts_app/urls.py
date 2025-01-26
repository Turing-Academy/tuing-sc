from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'classrooms', views.ClassroomViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'lessons', views.LessonScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]