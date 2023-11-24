import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data from CSV
read_data = pd.read_csv('random_data.csv')

# Define a custom color palette for different categories
palette = sns.color_palette("Set2", n_colors=len(read_data['Category'].unique()))

# Create a swarm plot with different colors for each category and different shades for positive and negative values
sns.swarmplot(x='Category', y='Value', data=read_data, hue='Category',
              palette=palette, alpha=0.7, edgecolor='black', linewidth=0.5, size=8)

# Add a dashed line to separate positive and negative values
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)

# Show the plot
plt.show()
