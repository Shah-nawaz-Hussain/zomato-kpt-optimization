import numpy as np

def detect_bias(df):

    diff = abs(df["for_time"] - df["rider_arrival_time"])

    biased_ratio = np.mean(diff < 1)

    return biased_ratio