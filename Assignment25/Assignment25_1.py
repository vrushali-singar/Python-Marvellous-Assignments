#Detect outliers in the 'Salary' column using the IQR method.
import pandas as pd
import numpy as np
def main():
    line = 50*"*"
    data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}
    df = pd.DataFrame(data)
    print(df)
    print(line)
    sort_data = np.sort(df["Salary"].to_numpy())
    print("sorted data:",sort_data)
    
    Q1 = np.percentile(df["Salary"], 25)
    Q2 = np.percentile(df["Salary"], 50)
    Q3 = np.percentile(df["Salary"], 75)
    print("Q1(25%)",Q1)
    print("Q2(50%)",Q2)
    print("Q3(75%)",Q3)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    print("Interquartile Range (IQR):", IQR)
    print("Lower bound:", lower_bound)
    print("Upper bound:", upper_bound)
    print(line)

    # Detect outliers
    outliers = df[(df["Salary"] < lower_bound) | (df["Salary"] > upper_bound)]
    if outliers.empty:
        print("No outliers detected.")
    else:
        print("Detected outliers:")
        print(outliers)

if __name__ == "__main__":
    main()