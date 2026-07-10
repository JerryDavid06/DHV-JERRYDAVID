import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
'Day':[1,2,3,4,5]*3,
'Temperature':[32,33,34,35,34,
               28,29,30,31,30,
               35,36,37,36,35],
'City':['Chennai']*5 +
      ['Bangalore']*5 +
      ['Delhi']*5
})

sns.lineplot(data=data,
             x='Day',
             y='Temperature',
             hue='City',
             style='City',
             markers=True)

plt.title("Temperature Trends")

plt.savefig("scenario4.png", dpi=300, bbox_inches="tight")
plt.show()
