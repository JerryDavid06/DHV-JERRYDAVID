import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ratings = pd.DataFrame({
'2023':[4.1,4.5,3.9,4.3],
'2024':[4.3,4.7,4.0,4.5],
'2025':[4.4,4.8,4.2,4.6]
},
index=['Action','Comedy','Drama','Sci-Fi'])

sns.heatmap(ratings,
            annot=True,
            cmap='YlGnBu')

plt.title("Movie Ratings")

plt.savefig("scenario8.png", dpi=300, bbox_inches="tight")
plt.show()
