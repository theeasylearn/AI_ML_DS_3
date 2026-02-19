import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Load dataset
data = pd.read_csv('t20.csv')
# Drop rows where age or survived is missing
data = data.dropna(subset=['Year', 'Wins'])

# Create lineplot: average survival by age
sns.lineplot(x='Year', y='Wins', data=data)

# Add labels and title
plt.title('T20 INDIA match wins')
plt.xlabel('Year')
plt.ylabel('Wins')
plt.show()
