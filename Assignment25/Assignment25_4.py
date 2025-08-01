#Apply One-Hot Encoding to a 'Department' column.
import pandas as pd

data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
df = pd.DataFrame(data)

# One-hot encode
df_encoded = pd.get_dummies(df, columns=['Department'], prefix='Dept')

print(df_encoded)