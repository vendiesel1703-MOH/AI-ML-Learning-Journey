# Bar Chart using Matplotlib

## What is a Bar Chart?

A Bar Chart is used to compare values across different categories.

## Example

```python
import matplotlib.pyplot as plt

subjects = ["Python", "NumPy", "Pandas", "ML"]
scores = [85, 78, 90, 88]

plt.bar(subjects, scores)
plt.title("Learning Progress")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()
```

## Output

The chart displays vertical bars representing scores for each subject.

## Applications

- Comparing categories
- Sales analysis
- Student performance
- Data Science dashboards

## What I Learned Today

Bar charts help compare different categories effectively and are widely used in analytics.
