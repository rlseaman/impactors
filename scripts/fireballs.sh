#!/bin/bash
# Query the CNEOS fireball database (US government sensor detections) for each impact date.
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
