import pandas as pd
import re

data = {
    "text": [
        "Hello World! @Python",
        "AI & ML are Amazing!!",
        "Data Science #1"
    ]
}

df = pd.DataFrame(data)

df["clean_text"] = df["text"].str.lower()
df["clean_text"] = df["clean_text"].apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", x))
df["tokens"] = df["clean_text"].apply(lambda x: x.split())

print(df)