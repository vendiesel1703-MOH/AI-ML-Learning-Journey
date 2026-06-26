import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Age": [20, 21, 22],
    "City": ["Bangalore", "Mysore", "Hubli"]
}

df = pd.DataFrame(data)

new_df = df.drop(columns=["City"])

print(new_df)
