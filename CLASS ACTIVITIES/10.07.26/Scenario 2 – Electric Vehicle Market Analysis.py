import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Battery':[40,50,60,75,90],
    'Price':[12,15,18,22,28],
    'Range':[250,300,380,450,520],
    'Manufacturer':['Tata','MG','Hyundai','Mahindra','BYD']
})

sns.scatterplot(data=data,
                x='Battery',
                y='Price',
                hue='Manufacturer',
                size='Range',
                sizes=(100,500))

plt.title("Battery Capacity vs Price")
plt.xlabel("Battery Capacity (kWh)")
plt.ylabel("Price (Lakhs)")

plt.savefig("scenario2.png", dpi=300, bbox_inches="tight")
plt.show()
