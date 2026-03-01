from data.simulator import generate_orders
from signals.bias_detector import detect_bias
from signals.signal_cleaner import clean_for_signal
from signals.kitchen_rush_index import compute_kri
from models.kpt_predictor import train_model, predict
from dispatch.smart_dispatch import smart_dispatch
from evaluation.metrics import evaluate

def main():

    df = generate_orders()

    bias_ratio = detect_bias(df)
    print("Merchant Bias Ratio:", bias_ratio)

    df = clean_for_signal(df)

    df = compute_kri(df)

    model = train_model(df)

    df = predict(model, df)

    df = smart_dispatch(df)

    results = evaluate(df)

    print("\nFinal Evaluation Metrics:")
    for k, v in results.items():
        print(f"{k}: {round(v, 3)}")

if __name__ == "__main__":
    main()