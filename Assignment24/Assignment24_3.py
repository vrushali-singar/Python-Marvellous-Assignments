#Group students by gender and calculate average marks.
import pandas as pd
import numpy as np
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
    summary = df.groupby('Gender').agg(
    count=('Name', 'size'),
    avg_math=('Math', 'mean'),
    avg_science=('Science', 'mean'),
    avg_english=('English', 'mean')
    ).reset_index()
    print(summary)
if __name__ == "__main__":
    main()
