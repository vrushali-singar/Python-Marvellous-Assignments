#Plot a histogram of math marks.
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

    plt.figure(figsize=(7,9))
    plt.hist(df['Math'],bins=5,color='blue',edgecolor='black')
    plt.title("Histogram for Maths Marks")
    plt.xlabel("Marks")
    plt.ylabel("frequency")
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    main()
    



