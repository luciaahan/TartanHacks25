import pandas as pd
import numpy as np



def get_fce(course_no, prof_name = None):
    df_2024 = pd.read_csv("fce_data_2024.csv")
    df_2023 = pd.read_csv("fce_data_2023.csv")
    df_2022 = pd.read_csv("fce_data_2022.csv")
    df = pd.concat([df_2024, pd.concat([df_2023,df_2022])])
    if(type(course_no) == str):
        course_no = course_no_convert(course_no)
    #print(15122 in set(df["Num"]))
    try:
        course_data = df[df["Num"] == course_no]
    except:
        print("Error: Invalid Course Number")
    try:
        assert(sum(course_data["Instructor"].isin([prof_name])) > 0)
        course_data = course_data[course_data["Instructor"] == prof_name]
    except:
        course_data = course_data
    return np.mean(course_data["Hrs Per Week"])

def course_no_convert(course_no):
    new = ""
    for c in course_no:
        if c.isdigit():
            new = new + c
    return int(new)