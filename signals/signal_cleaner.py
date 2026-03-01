def clean_for_signal(df):

    df["cleaned_kpt"] = df["for_time"] - df["order_confirm_time"]

    # Remove rider-influenced noise
    mask = abs(df["for_time"] - df["rider_arrival_time"]) < 1

    df.loc[mask, "cleaned_kpt"] = (
        df["rider_arrival_time"] -
        df["order_confirm_time"] -
        df["rider_travel_time"]
    )

    return df