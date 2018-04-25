influx

```
docker run -p 8086:8086 -v $PWD/data:/var/lib/influxdb/data influxdb

```

python
```
python print_test.py
python compression_test.py

```

measuring

```
du -sh data/test            # 135M
du -sh data/json            # 141M
du -sh test.csv             # 136M
du -sh test.gzip.parquet    # 38M
```
