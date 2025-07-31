#Export the final DataFrame to a CSV file.
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
    print(line)

    df['Total'] = df[["Math",'Science','English']].sum(axis=1)
    df["Status"]= df["Total"].apply(lambda x:'Pass' if x>=250 else 'Fail')
    print("Total and statues cols added")
    print(df)
    
    df.to_csv("Assignment24_7.csv",index=False)
    #index=False avoids writing the DataFrame’s row index to the CSV file.

    print("DataFrame exported to 'student_results.csv' successfully!")
if __name__ == "__main__":
    main()
