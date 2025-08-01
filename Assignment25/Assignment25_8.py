#Fill missing values in a numeric column using interpolation.
import pandas as pd
import numpy as np
def main():
    line = "**"*30
    data = {'Marks': [85, np.nan, 90, np.nan, 95]}
    df = pd.DataFrame(data)
    print(df)
    print(line)
    df['Marks_interpolated'] = df['Marks'].interpolate()
    print(df)
if __name__ == "__main__":
    main()


