import pandas as pd

data = {
    "Student": ["A", "B", "C", "D"],
    "Marks": [65, 92, 75, 88]
}

df = pd.DataFrame(data)

sorted_df = df.sort_values(by="Marks", ascending=False)

print(sorted_df)
