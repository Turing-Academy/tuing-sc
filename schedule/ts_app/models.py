# models.py
from django.db import models

class Classroom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    DAY_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LessonSchedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='lessons')
    day = models.CharField(max_length=3, choices=Group.DAY_CHOICES)
    time = models.TimeField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)


class RecordLink(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
