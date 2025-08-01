#Split a DataFrame with multiple features into train-test for supervised learning.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
def main():
    data = {
    'Age': [25, 30, 45, 35, 22],
    'Salary': [50000, 60000, 80000, 65000, 45000],
    'Purchased': [1, 0, 1, 0, 1]
    }
    df = pd.DataFrame(data)
    print(df)

    X = df[["Age","Salary"]] #features
    Y = df["Purchased"]  #label
    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    train_df = pd.concat([x_train.reset_index(drop=True), y_train.reset_index(drop=True)], axis=1)
    test_df = pd.concat([x_test.reset_index(drop=True), y_test.reset_index(drop=True)], axis=1)

    print("Train set:")
    print(train_df)
    print("\nTest set:")
    print(test_df)
if __name__ == "__main__":
    main()