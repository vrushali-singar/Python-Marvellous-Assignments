import pandas as pd
import numpy as np
def main():
    line=80*'*'
    data = {
        'Name':['Amit','sagar','Pooja'],
        'Math':[np.nan,90,75],
        'Science': [92, np.nan, 80]
        }
    df = pd.DataFrame(data)
    print("student marks in dataframe:")
    print(df)
    print(line)
    
    df.fillna(df.mean(numeric_only=True),inplace=True)
    print(df)



    
if __name__ == "__main__":
    main()