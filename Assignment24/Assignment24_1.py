#Normalize the 'Math' scores using Min-Max scaling.
"""Min-Max Scaling (also called Min-Max Normalization) is a data normalization 
technique used to rescale values into a fixed range, usually 0 to 1.

x scaled = x−min(x)/max(x)−min(x)

min(x) = smallest value in the column
max(x) = largest value in the column

After scaling:
Minimum value → 0
Maximum value → 1
All other values → proportionally between 0 and 1

Example
Original Math scores: [85, 90, 75]
Min = 75
Max = 90
Normalize each:
85→(85−75)/(90−75)=10/15≈0.667
90→(85−75)/(90−75)=10/15≈0.667
75→(75−75)/15=0
Result: [0.667, 1.0, 0.0]"""

import pandas as pd
import numpy as np

def min_max_math(series: pd.Series) -> pd.Series:
    min_value = series.min()
    max_value = series.max()
    if max_value == min_value:
        return pd.Series(0.0,index=series.index)
    return (series - min_value)/(max_value-min_value)


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
    df['Math_normalized'] = min_max_math(df['Math'])
    print("Student marks with Min-Max normalized 'Math' scores:")
    print(df)
    
if __name__ == "__main__":
    main()