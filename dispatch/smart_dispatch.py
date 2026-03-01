from config.settings import DISPATCH_BUFFER_MINUTES

def smart_dispatch(df):

    df["dispatch_time"] = (
        df["order_confirm_time"]
        + df["predicted_kpt"]
        - df["rider_travel_time"]
        - DISPATCH_BUFFER_MINUTES
    )

    df["arrival_time"] = df["dispatch_time"] + df["rider_travel_time"]

    df["rider_wait_time"] = (
        df["order_confirm_time"] + df["true_kpt"]
        - df["arrival_time"]
    )

    df["rider_wait_time"] = df["rider_wait_time"].clip(lower=0)

    return df