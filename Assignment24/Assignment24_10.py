#Plot a boxplot for English marks to check distribution and outliers.

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
    print(line)

    plt.figure(figsize=(6,7))
    plt.boxplot(df['English'],patch_artist=True, boxprops=dict(facecolor='lightblue'))
    plt.title("Box plot for  English Marks")
    plt.ylabel("Marks")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()
    

   
    
if __name__ == "__main__":
    main()