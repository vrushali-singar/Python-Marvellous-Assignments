import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

    marks = df[df["Name"] == 'Amit'][['Math','Science','English']].values.flatten()
    #print(marks)
    subjects =['Math','Science','English']
    plt.plot(subjects,marks,marker='o')
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.title("amit report")
    plt.show()
    
if __name__ == "__main__":
    main()