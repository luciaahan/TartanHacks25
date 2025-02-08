from openai import OpenAI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

class cal_time(BaseModel):
  hwTimes: list[str]
  studytimes: list[str]
  lectureTime: list[str]

def generate_schedule(data):
  ai_api_key = os.getenv("GEN_SCHEDULE_KEY")
  client = OpenAI(
    api_key = ai_api_key
  )

  system_prompt = '''
  You are a academic advisor of this student. You strongly want them to succeed academically. 
  You have access to all the academic information of the student
  including their preferences such as how many hours they can dedicate to studying, 
  how they want to allocate their study time for major exams,
  how they want to balance time between assignments and studying for exams 
  and what times of the day they prefer to study, how long they want the study sessions to be.
  You also have access to their lecture times, homework due dates, exam dates, 
  attendance policy, late day policy and weights of each grade category. 
  Your goal is to plan out their week from February 10th to 16th 
  by adding in studying hours for each classes while 
  following the students' preferences.
  You also have access to fce of the course, which is the expected number of hours
  spent a week for a course. 
  Considering all these factors, your output should look like this:
  Event Name without spaces YYYY-MM-DD HH:MM - HH:MM
  hwTimes = ['CourseName HW1 2025-02-13 11:00 - 13:45', 'CourseName HW2 2025-02-15 18:00 - 21:45'] 
  studytimes = ['CourseName Study 2025-02-14 15:00 - 17:00', 'CourseName Study 2025-02-15 19:00 - 22:30'] 
  '''
  response = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    store=True,
    messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": data}
    ],
    response_format = cal_time
  )
  return response.choices[0].message.parsed


def main(data):
  load_dotenv()  # Load environment variables from .env

  result = generate_schedule(str(data))
  return result