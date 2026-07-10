import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
'RAM':[4,6,8,12,16],
'Price':[15000,22000,30000,45000,65000],
'Storage':[64,128,128,256,512],
'Processor':[2.0,2.2,2.4,2.8,3.1],
'Brand':['Samsung','Realme','Vivo','OnePlus','Apple']
})

sns.scatterplot(data=data,
                x='RAM',
                y='Price',
                hue='Processor',
                size='Storage',
                style='Brand',
                sizes=(100,500))

plt.title("Smartphone Comparison")

plt.savefig("scenario7.png", dpi=300, bbox_inches="tight")
plt.show()
