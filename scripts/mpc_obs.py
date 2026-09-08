# Fetch every observation for the 13 pre-discovered impactors from the MPC Explorer API
# and count observations and distinct station codes per object. Writes data/mpc_observations.json.
import json, urllib.request, collections, sys
objs = ["2008 TC3","2014 AA","2018 LA","2019 MO","2022 EB5","2022 WJ1","2023 CX1","2024 BX1","2024 RW1","2024 UQ","2024 XA1","2026 JN4","2026 RW1"]
out = {}
for o in objs:
    req = urllib.request.Request("https://data.minorplanetcenter.net/api/get-obs",
        data=json.dumps({"desigs":[o],"output_format":["obs80"]}).encode(),
        headers={"Content-Type":"application/json"}, method="GET")
    try:
        r = json.load(urllib.request.urlopen(req, timeout=120))
    except Exception as e:
        print(o, "ERR", e); continue
    rec = r[0] if isinstance(r, list) else r
    lines = [l for l in rec.get("obs80","").split("\n") if len(l) >= 80]
    stations = collections.Counter(l[77:80] for l in lines)
    dates = sorted(l[15:32] for l in lines)
    disc = [l for l in lines if l[12] == '*']
    out[o] = {"nobs": len(lines), "nsta": len(stations), "stations": dict(stations),
              "first": dates[0] if dates else None, "last": dates[-1] if dates else None,
              "disc": [(l[15:32], l[77:80]) for l in disc]}
    print("%-9s nobs=%4d nsta=%2d first=%s last=%s disc=%s" % (o, len(lines), len(stations), out[o]["first"], out[o]["last"], out[o]["disc"]))
    print("          ", " ".join("%s(%d)" % kv for kv in stations.most_common()))
json.dump(out, open("data/mpc_observations.json","w"), indent=1)
