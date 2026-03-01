import numpy as np
import pandas as pd
from config.settings import NUM_ORDERS

def generate_orders():

    np.random.seed(42)

    data = []

    for i in range(NUM_ORDERS):

        order_confirm_time = np.random.randint(0, 1440)

        true_kpt = np.random.normal(15, 5)
        true_kpt = max(5, true_kpt)

        rider_travel_time = np.random.normal(10, 3)
        rider_travel_time = max(3, rider_travel_time)

        rider_arrival_time = order_confirm_time + rider_travel_time

        # Merchant bias simulation
        if np.random.rand() < 0.5:
            for_time = rider_arrival_time + np.random.normal(0, 1)
        else:
            for_time = order_confirm_time + true_kpt + np.random.normal(0, 2)

        data.append([
            order_confirm_time,
            true_kpt,
            rider_travel_time,
            rider_arrival_time,
            for_time
        ])

    df = pd.DataFrame(data, columns=[
        "order_confirm_time",
        "true_kpt",
        "rider_travel_time",
        "rider_arrival_time",
        "for_time"
    ])

    return df