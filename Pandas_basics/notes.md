# Pandas Basics

## What is Pandas?

Pandas is a Python library used for data manipulation and analysis. It helps work with tables, datasets, and structured data.

## Why Pandas?

- Easy data handling
- Data cleaning and preprocessing
- Supports CSV, Excel, and database files
- Widely used in Data Science and Machine Learning

## Creating a DataFrame

```python
import pandas as pd

data = {
    "Name": ["Mohit", "Rahul", "Aman"],
    "Age": [21, 22, 20]
}

df = pd.DataFrame(data)
print(df)
```

Output:

```text
    Name  Age
0  Mohit   21
1  Rahul   22
2   Aman   20
```

## What I Learned Today

- Pandas is used for data analysis
- DataFrame is the main data structure
- Pandas simplifies working with tabular data

## Next Topics

- Reading CSV files
- Data Selection
- Filtering Data
- Data Cleaning
