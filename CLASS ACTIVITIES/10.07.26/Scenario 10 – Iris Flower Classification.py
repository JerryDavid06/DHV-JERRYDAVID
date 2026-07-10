import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.scatterplot(data=iris,
                x='sepal_length',
                y='petal_length',
                hue='species',
                style='species',
                size='sepal_width',
                sizes=(30,250))

plt.title("Iris Flower Classification")

plt.savefig("scenario10.png", dpi=300, bbox_inches="tight")
plt.show()
