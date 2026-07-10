import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
'State':['TN','KA','KL','AP','TS'],
'Cases':[1200,1800,900,1500,1100]
})

pivot = data.set_index('State').T

sns.heatmap(pivot,
            annot=True,
            cmap='Reds')

plt.title("COVID Active Cases")

plt.savefig("scenario9.png", dpi=300, bbox_inches="tight")
plt.show()
