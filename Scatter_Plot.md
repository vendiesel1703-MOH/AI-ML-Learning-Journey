# Scatter Plot in Matplotlib

## What is a Scatter Plot?

A scatter plot is used to show the relationship between two numerical variables.

## Example

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
