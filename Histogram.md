# Histogram using Matplotlib

## What is a Histogram?

A Histogram is used to show the distribution of numerical data by dividing values into ranges called bins.

## Example

```python
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

plt.hist(marks, bins=5)
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
```

## Output

The histogram displays how frequently values occur within specific ranges.

## Applications

- Data Distribution Analysis
- Understanding Frequency Patterns
- Detecting Outliers
- Exploratory Data Analysis (EDA)

## What I Learned Today

Histograms help visualize the distribution and frequency of numerical data.

## Next Topics

- Scatter Plot
- Pie Chart
- Seaborn Basics
