#!/bin/bash
# Query the CNEOS fireball database (US government sensor detections) for each impact date.
for d in 2008-10-07 2014-01-02 2018-06-02 2019-06-22 2022-03-11 2022-11-19 2023-02-13 2024-01-21 2024-09-04 2024-10-22 2024-12-03 2026-05-15 2026-09-06; do
  echo "== $d"
  curl -s "https://ssd-api.jpl.nasa.gov/fireball.api?date-min=${d}&date-max=${d}T23:59:59&req-loc=false" | python3 -c '
import sys,json
j=json.load(sys.stdin)
f=j.get("fields",[]); 
for r in j.get("data",[]): print(dict(zip(f,r)))
print("count",j.get("count"))'
done
echo "== latest 5 entries overall"
curl -s "https://ssd-api.jpl.nasa.gov/fireball.api?limit=5" | python3 -c '
import sys,json
j=json.load(sys.stdin); f=j["fields"]
for r in j["data"]: print(dict(zip(f,r)))'
