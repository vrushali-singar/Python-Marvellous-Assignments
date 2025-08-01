#Replace multiple values in a column using a dictionary.
#Replace as'A+': 'Excellent''A': 'Very Good''B+': 'Good''B': 'Average''C': 'Poor'
import pandas as pd
def main():
    data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}
    df = pd.DataFrame(data)
    replace_values ={'A+': 'Excellent','A': 'Very Good',
                     'B+': 'Good','B': 'Average','C': 'Poor'}
    df['Grade']= df['Grade'].replace(replace_values)
    print(df)
if __name__ == "__main__":
    main()




