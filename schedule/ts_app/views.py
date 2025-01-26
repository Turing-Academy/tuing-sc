from rest_framework import viewsets
from .models import *
from .serializers import *

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.prefetch_related('teachers', 'lessons').all()
    serializer_class = GroupSerializer

class LessonScheduleViewSet(viewsets.ModelViewSet):
    queryset = LessonSchedule.objects.all()
    serializer_class = LessonScheduleSerializer

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
