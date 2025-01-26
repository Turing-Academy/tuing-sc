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

class Teacher(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='teachers')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teachers/', null=True, blank=True)

class TeacherImage(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='teacher_images/')

class LessonSchedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='lessons')
    day = models.CharField(max_length=3, choices=Group.DAY_CHOICES)
    time = models.TimeField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
