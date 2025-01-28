# serializers.py
from rest_framework import serializers
from .models import *

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class LessonScheduleSerializer(serializers.ModelSerializer):
    classroom = serializers.CharField(source='classroom.name', read_only=True)

    class Meta:
        model = LessonSchedule
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    lessons = LessonScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'


class RecordLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordLink
        fields = '__all__'
