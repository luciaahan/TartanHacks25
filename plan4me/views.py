from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from plan4me.models import CourseInfo

from openai import OpenAI
import fitz
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import parse_syllabus


def global_action(request):
    return redirect('home')

def get_started_action(request):
    if request.method == 'GET':
        return render(request, 'plan4me/get_started.html', context={'message': ''})
    
    # parse syllabus
    pdf_file = 'syllabus.pdf' # replace with pdf file uploaded
    
    # ChatGPT response
    extracted_data = parse_syllabus.parseThis(pdf_file)
    new_course_info = get_object_or_404(CourseInfo, id=id)

    new_course_info.course_name = extracted_data.className
    new_course_info.course_number = extracted_data.classNumber
    new_course_info.lecture_time = extracted_data.lectureTime
    new_course_info.hw_dates = extracted_data.hwDates
    new_course_info.exam_dates = extracted_data.examDates
    new_course_info.late_day = extracted_data.lateday
    new_course_info.attendance = extracted_data.attendance
    new_course_info.grade_weight = extracted_data.gradeWeight
    
    new_course_info.save()

    # click move on -> settings page
    # click add more classes -> same page
    return render(request, 'plan4me/get_started.html', context={'message': ''})


def settings_action(request):
    if request.method == "GET":
        return render(request, 'plan4me/settings.html')

    time_option = request.POST.get('time_option') # user input
    
    # pass course FCEs into chatGPT
    # pass options into chatGPT to generate calendar


    # click generate schedule -> generate schedule page
    return render(request, 'plan4me/generate_schedule.html')


def generate_schedule_action(request):

    return render(request, 'plan4me/generate_schedule.html')


