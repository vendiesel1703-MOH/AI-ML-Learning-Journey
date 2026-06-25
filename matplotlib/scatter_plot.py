import matplotlib.pyplot as plt

# Sample data
hours_studied = [1, 2, 3, 4, 5, 6, 7]
marks = [35, 42, 50, 60, 68, 80, 90]

plt.scatter(hours_studied, marks, color="blue", marker="o")

plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")

plt.grid(True)

plt.show()
