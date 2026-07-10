import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Attendance':[75,80,85,90,95,70,88,92],
    'Marks':[65,72,78,85,95,60,82,90],
    'Department':['CSE','AI','IT','ECE','CSE','AI','IT','ECE']
})

sns.scatterplot(data=data,
                x='Attendance',
                y='Marks',
                hue='Department',
                s=120)

plt.title("Student Academic Performance")
plt.xlabel("Attendance (%)")
plt.ylabel("Internal Marks")

plt.savefig("scenario1.png", dpi=300, bbox_inches="tight")
plt.show()
