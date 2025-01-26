from rest_framework import serializers
from .models import *

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class TeacherImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherImage
        fields = ['image']

class LessonScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonSchedule
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    images = TeacherImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Teacher
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    lessons = LessonScheduleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Group
        fields = '__all__'