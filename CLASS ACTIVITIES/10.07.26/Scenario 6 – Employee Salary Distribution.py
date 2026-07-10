import numpy as np
import matplotlib.pyplot as plt

salary = np.random.randint(25000,100000,300)

plt.hist(salary, bins=10)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.savefig("scenario6.png", dpi=300, bbox_inches="tight")
plt.show()
