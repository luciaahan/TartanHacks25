from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from plan4me.models import CourseInfo

from plan4me.forms import UploadFileForm
import plan4me.parse_syllabus as parse_syllabus
import create_schedule as create_schedule
import calendar_generator as calendar_generator
from fce import get_fce


def global_action(request):
    return render(request, 'plan4me/index.html')

def get_started_action(request):
    if request.method == 'GET':
        return render(request, 'plan4me/getstarted.html', context={'message': ''})
    
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        file_path = request.FILES["file"]

    # parse syllabus
    # pdf_file = file_path
    pdf_file = 'syllabus_writing.pdf' # replace with pdf file uploaded
    
    # ChatGPT response
    extracted_data = parse_syllabus.parseThis(pdf_file)

    print("extractedData: ", extracted_data)

    new_course_info = CourseInfo()

    print("new_course_info: ", new_course_info)
    new_course_info.course_name = extracted_data.className
    new_course_info.course_number = extracted_data.classNumber
    new_course_info.lecture_time = extracted_data.lectureTime
    new_course_info.hw_dates = extracted_data.hwDates
    new_course_info.exam_dates = extracted_data.examDates
    new_course_info.late_day = extracted_data.lateday
    new_course_info.attendance = extracted_data.attendance
    new_course_info.grade_weight = extracted_data.gradeWeight
    new_course_info.fce = get_fce(extracted_data.classNumber)
    
    new_course_info.save()

    courses = CourseInfo.objects.all()

    for course in courses:
        print("all:::", course)
    # click move on -> personalize page
    # click add more classes -> same page
    # return render(request, 'plan4me/personalize.html')

    if request.POST.get('action') == "add_more":
        return redirect('get-started')
    elif request.POST.get('action') == "next_step":
        return redirect('personalize')


def personalize_action(request):
    if request.method == "GET":
        schedule_result = create_schedule.main(CourseInfo.objects.all()) # caltime format
        calendar_generator.create_calendar(schedule_result)

        return render(request, 'plan4me/generatedschedule.html')

    # pass course FCEs into chatGPT
    # pass options into chatGPT to generate calendar


    # click generate schedule -> generate schedule page
    return render(request, 'plan4me/generatedschedule.html')


def generate_schedule_action(request):

    return render(request, 'plan4me/generatedschedule.html')


