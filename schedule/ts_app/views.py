from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serializers import *

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.prefetch_related('lessons').all()
    serializer_class = GroupSerializer


class LessonScheduleViewSet(viewsets.ModelViewSet):
    queryset = LessonSchedule.objects.all()
    serializer_class = LessonScheduleSerializer


class RecordLinkViewSet(viewsets.ModelViewSet):
    queryset = RecordLink.objects.all().order_by('-created_at')
    serializer_class = RecordLinkSerializer

    @action(detail=False, methods=['get'], url_path='last')
    def last(self, request):
        latest_record = self.queryset.first()
        if latest_record:
            serializer = self.get_serializer(latest_record)
            return Response(serializer.data)
        return Response({"detail": "No records found"}, status=404)
    
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
