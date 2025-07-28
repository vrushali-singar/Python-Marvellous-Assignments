import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def main():
    line = 80*'*'
    data = {
        'Name':['Amit','sagar','Pooja'],
        'Math':[85,90,75],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    print("orginal data: student marks in dataframe:")
    print(df)
    print(line)

    df["Total"]=df['Math']+df['Science']+df['English']

    plt.bar(df['Name'],df['Total'])
    plt.xlabel("STudent name")
    plt.ylabel("Total Marks")
    plt.title("Bar plot")
    plt.show()


    
if __name__ == "__main__":
    main()