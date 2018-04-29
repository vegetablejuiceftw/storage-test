influx

```
docker run -p 8086:8086 -v $PWD/data:/var/lib/influxdb/data influxdb

```

python
```
python format_test.py
python compression_test.py

```

### measuring

each ticker on separate row

```
du -sh data/test            # 135M
du -sh data/json            # 141M
du -sh test.csv             # 136M
du -sh test.gzip.parquet    # 38M
```

10K columns and wow

```
du -sh data/test            # 122M
du -sh data/json            # 125M
du -sh test.csv             # 1300M
du -sh test.gzip.parquet    # 64M
```
