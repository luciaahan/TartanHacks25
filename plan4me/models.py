from django.db import models


class CourseInfo(models.Model):
    course_name = models.CharField(max_length=100)
    course_number = models.CharField(max_length=5)
    lecture_time = models.TextField(blank=True, null=True)
    hw_dates = models.TextField(blank=True, null=True)
    exam_dates = models.TextField(blank=True, null=True)
    late_day = models.CharField(max_length=10)
    attendance = models.TextField(blank=True, null=True)
    grade_weight = models.TextField(blank=True, null=True)
    fce = models.CharField(blank=True, max_length=5)


