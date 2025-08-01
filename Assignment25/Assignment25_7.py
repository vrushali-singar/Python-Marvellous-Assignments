# Normalize 'Age' column using Min-Max Scaling.
import pandas as pd
def main():
    data = {'Age': [18, 22, 25, 30, 35]}
    df = pd.DataFrame(data)
    print(df)
    min_val = df["Age"].min()
    max_val = df["Age"].max()
    df["Age_normalized"] = (df["Age"]- min_val)/(max_val-min_val)
    print(df)
if __name__ == "__main__":
    main()

