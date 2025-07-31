#Create a gender column and perform one-hot encoding

import pandas as pd
import numpy as np
def main():
    line = "*"*50
    data = {
        'Name':['Amit','sagar','Pooja'],
        'Math':[85,90,75],
        'Science': [92, 88, 80],
        'English': [75, 85, 82],
        'Gender': ['M', 'M', 'F']
    }
    df = pd.DataFrame(data)
    print("student marks in dataframe:")
    print(df)
    df['Gender'] = df['Gender'].map({'F':0,'M':1})
    print(line)
    print("Encode data is:")
    print(df)
if __name__ == "__main__":
    main()