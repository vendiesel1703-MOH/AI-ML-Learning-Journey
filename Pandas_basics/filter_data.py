import pandas as pd

data = {
    "Name": ["Mohit", "Rahul", "Ananya", "Riya"],
    "Age": [21, 19, 22, 20],
    "Marks": [88, 65, 92, 75]
}

df = pd.DataFrame(data)

# Students scoring above 80
filtered = df[df["Marks"] > 80]

print(filtered)
