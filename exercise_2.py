import sqlite3

import pandas as pd
from contextlib import closing

def last_error_time(df):
    """
    Find last time there is an error in df
    """
    last_time = None
    for _ , row in df.iterrows():
        if row['status_code'] < 400:
            continue
        if not last_time or row['time'] > last_time:
            last_time = row['time']
    return last_time

    