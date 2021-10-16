import numpy as np
from typing import List

def parse_school_array(school_array):
    school_list = []
    prio_list = []
    date_list = []
    for row in school_array:
        prio_list.append(row[1])
        school_list.append(row[0])
        for date in range(len(row)-2):
            if len(row[date+2]) > 2:
                date_list.append(row[date+2])

    return np.array(school_list), date_list, np.array(prio_list)

def get_unique_date_list(date_list: str) -> List[str]:
    unique_dates = []
    for date in date_list:
        if date not in unique_dates:
            unique_dates.append(date)
    return unique_dates

def get_schedule_value(prio_list, school_choice_dict):
    chosen_list = list(school_choice_dict.values())
    value = (prio_list.T @ chosen_list).sum()
    return value 
    