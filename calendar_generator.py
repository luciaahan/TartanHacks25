from ics import Calendar, Event
from datetime import datetime
import parse_syllabus
from fce import get_fce

def create_calendar(schedule):
    '''
    Syllabus is a list of strings with the information in the following format
    "[Event Name (without spaces)] YYYY-MM-DD HH:MM - HH:MM"
    The string will then be transformed so that it can be updated to the calendar
    This calendar will be saved as a .ics file
    '''
    c = Calendar()
    for event in schedule.hwTimes:
        e = create_event(event)
        c.events.add(e)
    
    for event in schedule.studytimes:
        e = create_event(event)
        c.events.add(e)

    for event in schedule.lectureTime:
        e = create_event(event)
        c.events.add(e)
    # hw_dates = syllabus.hwDates
    # exam_dates = syllabus.examDates
    # lecture_time = syllabus.lectureTime

    # fce = get_fce(class_name)

    # lecture_events = lecture_to_datetime(lecture_time, syllabus.classNumber)
    # for e in lecture_events:
    #     c.events.add(e)

    with open('media/calendars/my.ics', 'w') as f:
         f.writelines(c.serialize_iter())

'''
def class_to_int(class_name):
    new_class = ""
    for c in class_name:
        if c.isdigit():
            new_class += c
    if(len(new_class) != 5):
        raise Exception("Class name is not in the correct format")
    return int(new_class)
'''
    
def create_event(event):
    event_info = event.split(" ")
    
    name = ""
    for i in range(len(event_info) - 4):
        name += event_info[i] + " "
    print(name)
    e = Event()
    e.name = name
    date = event_info[-4]
    start_time = event_info[-3]
    end_time = event_info[-1]
    e.begin = date + " " + start_time + ":00"
    e.end = date + " " + end_time + ":00"
    
    return e
    '''
    for lecture in lectures:
        info = lecture_time.split(" ")
        days = info[0]
        start_data = info[1].split(":")
        start_am_pm = info[2]
        if(start_am_pm == "PM" and int(start_am_pm[0]) < 12):
            start_data[0] = int(start_data[0]) + 12
        end_data = info[3].split(":")
        end_am_pm = info[4]
        if(end_am_pm == "PM" and int(end_am_pm[0]) < 12):
            end_data[0] = int(end_data[0]) + 12
        e = Event()
        e.name = str(lecture_number) + " Lecture"
        e.begin = datetime(2022, 1, 1, int(start_data[0]), int(start_data[1]))
        e.end = datetime(2022, 1, 1, int(end_data[0]), int(end_data[1]))
        lecture_events.append(e)
    return lecture_events
    '''