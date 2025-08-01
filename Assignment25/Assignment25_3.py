#Apply Label Encoding to a 'City' column.
import pandas as pd

data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
df = pd.DataFrame(data)

# Create mapping manually
mapping = {'Delhi': 0, 'Mumbai': 1, 'Pune': 2}
df['City_encoded'] = df['City'].map(mapping)

print(df)