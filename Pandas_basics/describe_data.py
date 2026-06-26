import pandas as pd

data = {
    "Age": [20, 21, 22, 23, 24],
    "Marks": [75, 80, 92, 88, 95]
}

df = pd.DataFrame(data)

print(df.describe())
