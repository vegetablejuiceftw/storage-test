import pandas as pd

df = pd.read_parquet("test.gzip.parquet")
df = df.fillna(0)

print(df.head(1))
print(df.dtypes)
print(df.index[:1])

# without index
# df.reset_index(drop=True, inplace=True)

# df.to_parquet('test2.gzip.parquet', compression='gzip')
# df.to_csv('test2.csv')
