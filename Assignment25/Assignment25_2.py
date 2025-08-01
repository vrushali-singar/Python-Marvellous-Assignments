#Detect column data types and convert 'Age' from float to int.
import pandas as pd
import numpy as np
def main():
    line = "**"*50
    data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}
    df = pd.DataFrame(data)
    print(df)
    print("coloumn datatype area :")
    print(df.dtypes)
    print(line)
    df['Age'] = df['Age'].astype(int)
    print("Age datatype changed from float to int")
    print(df.dtypes)
if __name__ == "__main__":
    main()
