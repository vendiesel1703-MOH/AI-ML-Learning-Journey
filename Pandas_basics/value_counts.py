import pandas as pd

data = {
    "Department": [
        "AI",
        "AI",
        "CSE",
        "AI",
        "ISE",
        "CSE"
    ]
}

df = pd.DataFrame(data)

print(df["Department"].value_counts())
