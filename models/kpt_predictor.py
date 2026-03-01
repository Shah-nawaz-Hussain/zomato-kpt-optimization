from sklearn.linear_model import LinearRegression

def train_model(df):

    X = df[["cleaned_kpt", "kri"]]
    y = df["true_kpt"]

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict(model, df):

    X = df[["cleaned_kpt", "kri"]]
    df["predicted_kpt"] = model.predict(X)

    return df