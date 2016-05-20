import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('penguins.csv')
data.boxplot(column='Depth (m)', by='Bird #')
plt.show()
