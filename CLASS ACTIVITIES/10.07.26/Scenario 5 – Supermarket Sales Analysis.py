import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
'Category':['Food','Food','Food',
            'Drinks','Drinks','Drinks',
            'Snacks','Snacks','Snacks'],
'Sales':[120,150,170,90,100,110,80,95,105],
'Branch':['A','B','C']*3
})

sns.barplot(data=data,
            x='Category',
            y='Sales',
            hue='Branch')

plt.title("Sales by Branch")

plt.savefig("scenario5.png", dpi=300, bbox_inches="tight")
plt.show()
