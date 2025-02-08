import pandas as pd
import numpy as np



def get_fce(course_no):
    df_2024 = pd.read_csv("fce_data_2024.csv")
    df_2023 = pd.read_csv("fce_data_2023.csv")
    df_2022 = pd.read_csv("fce_data_2022.csv")
    df = pd.concat([df_2024, pd.concat([df_2023,df_2022])])
    #print(15122 in set(df["Num"]))
    try:
        course_data = df[df["Num"] == course_no]
    except:
        print("Error: Invalid Course Number")
    #print(course_data)
    return np.mean(course_data["Hrs Per Week"])

