<h1> Plan4Me </h1>

<h2> Introduction </h2>
Are you a college student who can't manage your time? <br>
Are you tired of inputting your classes yourself? <br>
Do you always fail on making plan and adhering to it?

Then this website is for you!

This is Plan4Me, a website that helps you be on top of your tasks and academic works!

Input the syllabi for your classes, and Plan4Me will create a calendar with all academic events including lectures, assignment due dates, exam dates. <br>
It would also plan out your studying time, when to start your homework, and other things to keep you on track.

<h2> Installation </h2>
List of Modules to install. You can install in the virtual environment that you are using with <code>pip install</code>.
<ul>
  <li><code>ics</code></li>
  <li><code>django</code></li>
  <li><code>openai</code></li>
  <li><code>python-dotenv</code></li>
</ul>

<h2> How to Run </h2>
Run these commands:
<code>
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
</code>
Then put this link in your website. <br>
<a href = "http://localhost:8000/"> Local Host Page </a>

<h2> How Plan4Me Works </h2>
<h3> Step 1: Drop your Syllabus</h3>
Upload the pdf of your schedule using upload button.

<h3> Step 2: Input your preference</h3>
Answer the questionaire. <br>
<ul>
  <li>When do you want to study?</li>
  <li>How many hours do you want to study?</li>
  <li>What courses do you want to focus on?</li>
</ul>
<h3> Step 3: Your schedule is generated!</h3>
Using OpenAI API, we parse the syllabus. <br>
Then, with your preference and with data from <a href = "https://courses.scottylabs.org/">CMU Courses</a> of ScottyLabs, Plan4Me will generate a schedule for you. <br>
Plan4Me is prompt-engineered to be your personal academic advisor.
