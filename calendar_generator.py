from ics import Calendar, Event
from datetime import datetime

def create_calendar(syllabus):
    c = Calendar()
    with open('my.ics', 'w') as f:
        f.writelines(c.serialize_iter())
