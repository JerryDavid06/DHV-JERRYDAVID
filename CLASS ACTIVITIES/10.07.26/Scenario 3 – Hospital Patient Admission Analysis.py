import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Department':['Cardiology','Neurology','Orthopedics','Pediatrics'],
    'Patients':[120,90,140,110],
    'Cost':[45000,52000,38000,30000]
})

bars = plt.bar(data['Department'],
               data['Patients'],
               color=['red','blue','green','orange'])

for bar, cost in zip(bars, data['Cost']):
    plt.text(bar.get_x()+bar.get_width()/2,
             bar.get_height(),
             str(cost),
             ha='center')

plt.title("Hospital Admissions")
plt.ylabel("Patients")

plt.savefig("scenario3.png", dpi=300, bbox_inches="tight")
plt.show()
