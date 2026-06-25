import matplotlib.pyplot as plt

subjects = ["Python", "ML", "NLP", "DL"]
hours = [10, 8, 6, 4]

plt.pie(
    hours,
    labels=subjects,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Weekly Study Time Distribution")

plt.show()
