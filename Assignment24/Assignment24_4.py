#Plot a pie chart of subject marks for 'Sagar'.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

    sagar_data = df[df['Name'].str.lower()=='sagar'][['Math',"Science","English"]].iloc[0]

    plt.figure(figsize=(6,6))
    plt.pie(
        sagar_data,
        labels=sagar_data.index,
    )
    plt.title("Sagar's Subject Marks Distribution")
    plt.show()
if __name__ == "__main__":
    main()