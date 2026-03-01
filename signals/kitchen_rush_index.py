import numpy as np

def compute_kri(df):

    hourly_orders = df.groupby(df["order_confirm_time"] // 60).size()

    df["hour"] = df["order_confirm_time"] // 60

    df["kri"] = df["hour"].map(hourly_orders)

    df["kri"] = df["kri"] / df["kri"].max()

    return df