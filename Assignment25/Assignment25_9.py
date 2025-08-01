#Replace values in 'Marks' less than 50 with 'Fail' using where().
import pandas as pd
import numpy as np
def main():
    line = '**'*30
    data = {'Marks': [45, 67, 88, 32, 76]}
    df = pd.DataFrame(data)
    print(df)
    df['Result'] = df["Marks"].where(df['Marks']>=50,"Fail")
    print(df)
#where(condition, other) → keeps values where condition is True, otherwise replaces with other.
#Here, marks ≥ 50 are kept, otherwise replaced by "Fail".
if __name__ == "__main__":
    main()
