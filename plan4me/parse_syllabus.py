from openai import OpenAI
import fitz
from pydantic import BaseModel
import os
from dotenv import load_dotenv

class core_info(BaseModel):
  className: str
  classNumber: str
  lectureTime: str
  hwDates: str
  examDates: str
  lateday: str
  attendance: str
  gradeWeight: str

  
def text_2_pdf(pdf_path):
  doc = fitz.open(pdf_path)
  text = '\n'.join([page.get_text("text") for page in doc])
  return text

def analyze_text(text):

  client = OpenAI(
    api_key= os.getenv("OPENAI_API_KEY")
  )

  system_prompt = '''
  You will be provided with a text that is a syllabus of a course at Carnegie Mellon University. 
  You will read through the document and give me the necessary information. 
  For the return format, you have to follow these:
  - className is course name 
  - classNumber is course number
  - lectureTime is the day and time of the lectures
  - hwDates is due dates of all homeworks
  - examDates is dates of all exams
  - lateday is the policy for late assignments
  - attendance is the policy for attending lectures and recitations
  - gradeWeight is the weights and categories for each grading criteria
  All information related to grade should be in gradeWeight, not in other categories.
  '''
  response = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    store=True,
    messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": text}
    ],
    response_format = core_info
  )

  return response.choices[0].message.parsed

def parseThis(pdf_file):
  load_dotenv()  # Load environment variables from .env
  extracted_syllabus = text_2_pdf(pdf_file)
  extracted_data = analyze_text(extracted_syllabus)
  return extracted_data

