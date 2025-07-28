import pandas as pd
import numpy as np
def main():
    data = {
        'Name':['Amit','sagar','Pooja'],
        'Math':[85,90,75],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    print("student marks in dataframe:")
    print(df)
    
    df['Total']=df[['Math',"Science",'English']].sum(axis=1)
    df["Total2"]=df['Math']+df['Science']+df['English']
    print("After adding Total column")
    print(df)
if __name__ == "__main__":
    main()