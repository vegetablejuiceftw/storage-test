import pandas as pd

# parquet_file_name = "test.gzip.parquet"
parquet_file_name = "test-large.gzip.parquet"
csv_file_name = "/home/microwave/scraping/kucoin/backup/scrape_04_29_2018.csv"

# df = pd.read_parquet(parquet_file_name)

df = pd.read_csv(csv_file_name,
                 parse_dates=[0],
                 index_col='datetime')

# df.index = pd.to_datetime(df.index)
# df.index.rename('datetime', inplace=True)

# to fill empty columns with 0
df = df.fillna(0)

print(df.head(1))
print(df.dtypes)
print(df.index[:1])
print(len(df), "total")
df = df[df.index.notnull()]

# drop columns with no data inside
# df.dropna(axis=1, inplace=True)

print(len(df), "total after dropping empty indexes")
df.sort_index(inplace=True)
print("sorting index done")

# print("columns: ", list(df))


# without index
# df.reset_index(drop=True, inplace=True)

#
print("df.head")
df.head(100).to_csv('test2-100.csv')
print("df.to_csv")
df.to_csv('test2-large.csv')
print("df.to_parquet")
df.to_parquet('test2-large.gzip.parquet', compression='gzip')
