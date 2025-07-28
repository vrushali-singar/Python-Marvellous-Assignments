#Display students who scored more than 85 in Science.
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
    
    print("Students who scored more than 85 in Science:")
    print(df[df['Science'] > 85])
    
if __name__ == "__main__":
    main()