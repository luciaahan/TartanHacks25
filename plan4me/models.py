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


class PersonalizedOptions(models.Model):
    hours_study = models.CharField(max_length=20)
    allocate_study = models.CharField(max_length=100)
    balance = models.CharField(max_length=100)
    time_prefer = models.CharField(max_length=100)
    study_session = models.CharField(max_length=100)
