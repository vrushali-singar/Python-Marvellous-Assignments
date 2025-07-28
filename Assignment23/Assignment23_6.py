#sort
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
    print("student marks in dataframe:")
    print(df)
    print(line)
    df["Total2"]=df['Math']+df['Science']+df['English']
   
    df_new = df.sort_values(by='Total2',ascending=False)
    print("data after sorting")
    print(df_new)
    
if __name__ == "__main__":
    main()