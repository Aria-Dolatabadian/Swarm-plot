import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Read data from CSV
read_data = pd.read_csv('random_data.csv')
# Create a swarm plot with different colors for each category
sns.swarmplot(x='Category', y='Value', data=read_data, hue='Category', palette='Set2', legend=False)
# Show the plot
plt.show()
