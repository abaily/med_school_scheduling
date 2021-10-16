import numpy as np
from typing import List

def get_unique_date_list(date_list: str) -> List[str]:
    unique_dates = []
    for date in date_list:
        if date not in unique_dates:
            unique_dates.append(date)
    return unique_dates
