# Loading essential libraries

import pandas as pd
import numpy as np

csv_file = "/Users/bt/Documents/GITHUB/Faster_Pandas/faster-pandas-2832038-main/Ch01/challenge/bids.csv.xz"


def second(values):
    """
    Return second highest value
    In:[7,1,3,10]
    Out:10
    """
    top, second = -1, -1
    for value in values:
        if value > top:
            top, second = value, top
        elif value > second:
            second = value
    return second

def median_diff(csv_file):
    """
    Reading csv file to get the data and get median
    """
    df = pd.read_csv(csv_file)
    top1 = df.groupby('id')['price'].max()
    top2 = df.groupby('id')['price'].apply(second)
    diffs = top1 - top2
    return diffs.median()
