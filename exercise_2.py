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
        if not last_time or row['time'] > last_time:ß
            last_time = row['time']
    return last_time

def load_df(db_file):
    """Load DataFrame from database"""
    conn = sqlite3.connect(db_file,detect_types=sqlite3.PARSE_DECLTYPES)
    with closing(conn):
        return pd.read_sql('SELECT * FROM logs', conn)