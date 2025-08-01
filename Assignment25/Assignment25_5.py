#Create a DataFrame with 'Age' and 'Purchased' columns and split into train/test sets.
import pandas as pd
from sklearn.model_selection import train_test_split
def main():
    data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}
    df = pd.DataFrame(data)
    print(df)
    X = df['Age']
    Y = df['Purchased']
    x_train, x_test, y_train, y_test =train_test_split(X,Y,test_size=0.2,random_state=42)
    train_df = pd.concat([x_train.reset_index(drop=True), y_train.reset_index(drop=True)], axis=1)
    test_df = pd.concat([x_test.reset_index(drop=True), y_test.reset_index(drop=True)], axis=1)

    print("Train set:")
    print(train_df)
    print("\nTest set:")
    print(test_df)
if __name__ == "__main__":
    main()

