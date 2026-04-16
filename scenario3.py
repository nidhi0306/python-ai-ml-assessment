import pandas as pd

data = {
    "income": [50000, 52000, None, 51000, 53000, None, 52000]
}

df = pd.DataFrame(data)

skew_value = df["income"].dropna().skew()

if abs(skew_value) < 0.5:
    fill_value = df["income"].median()
else:
    fill_value = df["income"].mode()[0]

df["income"] = df["income"].fillna(fill_value)

print(df)