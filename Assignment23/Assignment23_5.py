import pandas as pd
import numpy as np
def main():
    line = 80*'*'
    data = {
        'Name':['Amit','sagar','Pooja'],
        'Math':[85,90,75],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    print("Original data :student marks in dataframe:")
    print(df)
    print(line)
    df["Name"] = df['Name'].replace('Pooja','Puja')
    print(df)
if __name__ == "__main__":
    main()