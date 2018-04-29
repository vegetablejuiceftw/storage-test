import json
from pprint import pprint

import pandas as pd
from influxdb import InfluxDBClient, DataFrameClient

df = pd.read_parquet("test2-large.gzip.parquet")
df = df.fillna(0)

print(df.dtypes)
print(df.index[:1])
print(len(df))

db_name = 'test_large_4'
 
# Testing dataframe client
# client = DataFrameClient('localhost', 8086, 'root', 'root', db_name)
# print(client)
# created = client.create_database(db_name)
# print(created)
#
# client.write_points(df, db_name, protocol="line", batch_size=100)
# print("influx done")
#

# testing json client
db_name = 'json_2'

client = InfluxDBClient('localhost', 8086, 'root', 'root', db_name)
client.create_database(db_name)
print("influx json start")

temp = []
for index, row in df.iterrows():
    body = json.loads(row.to_json())

    json_body = {
            "measurement": db_name,
            "time": index.isoformat(),
            "fields": body
        }

    temp.append(json_body)

    if len(temp) == 100:

        client.write_points(temp)

        temp = []

        print(index, index.isoformat())
        # pprint(json_body)
