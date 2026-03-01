import numpy as np

def evaluate(df):

    mae = np.mean(abs(df["true_kpt"] - df["predicted_kpt"]))

    avg_wait = np.mean(df["rider_wait_time"])

    p90_error = np.percentile(
        abs(df["true_kpt"] - df["predicted_kpt"]),
        90
    )

    return {
        "MAE_KPT": mae,
        "P90_Error": p90_error,
        "Avg_Rider_Wait_Time": avg_wait
    }