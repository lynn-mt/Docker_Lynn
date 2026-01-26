powimport sys
import pandas as pd
print('argument',sys.argv)
month = sys.argv[1]
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df['month'] = month
df.to_parquet(f"output_{month}.parquet")
print(df.head())
print(f'hello pipeline, month={month}')
