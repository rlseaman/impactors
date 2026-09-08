# Rank the 13 impactors by in-flight confidence (rank-sum of observations, telescopes,
# warning time, and U) and emit the Markdown table. Reads data/mpc_observations.json.
import json
from datetime import datetime, timedelta
mpc = json.load(open("data/mpc_observations.json"))
def mjd2dt(s):
    y,m,d = s.split(); dd=float(d); return datetime(int(y),int(m),int(dd)) + timedelta(days=dd-int(dd))
# object, disc code, discovery obs (MPC date string), impact UTC, U, evidence rank, evidence line1, line2, tier
rows = [
 ("2008 TC3","G96","2008 10 06.27767","2008-10-07 02:45:45",4,1,
  "Meteosat 8 flash, US sensors (1 kt), infrasound, KLM pilots; pre-impact spectrum and lightcurve",
  "600 Almahata Sitta stones, 10.5 kg (ureilite)","Meteorites"),
 ("2023 CX1","K88","2023 02 12.845917","2023-02-13 02:59:22",4,2,
  "FRIPON camera trajectory, thousands of witnesses across France and England",
  "Saint-Pierre-le-Viger stones, about 1 kg (L chondrite)","Meteorites"),
 ("2024 BX1","K88","2024 01 20.90865","2024-01-21 00:32:44",5,3,
  "Widely filmed over Berlin and Leipzig; no US sensor entry",
  "200+ Ribbeck stones, 1.8 kg (aubrite)","Meteorites"),
 ("2018 LA","G96","2018 06 02.34330","2018-06-02 16:44:12",6,4,
  "US sensors (0.9 kt), many dashcam and security videos in Botswana",
  "Motopi Pan stones, Central Kalahari (howardite)","Meteorites"),
 ("2024 RW1","G96","2024 09 04.238671","2024-09-04 16:39:32",5,5,
  "US sensors 0.2 kt at 18.0N 122.9E, matching ESA's 0.19 kt model",
  "Videos from Luzon through typhoon cloud; no stones","Sensor + video"),
 ("2022 WJ1","G96","2022 11 19.203482","2022-11-19 08:26:58",6,6,
  "All-sky camera trajectory, widespread video from Ontario and four US states",
  "Weather radar tracked falling stones into Lake Ontario; none recovered","Trajectory + radar"),
 ("2022 EB5","K88","2022 03 11.80848","2022-03-11 21:22:45",6,7,
  "US sensors 3.8 kt at 70.0N 9.1W; infrasound in Greenland and Norway",
  "Possible flash seen from northern Iceland; ESA model only 0.4 kt","Sensor"),
 ("2024 XA1","V00","2024 12 03.246721","2024-12-03 16:15:01",5,8,
  "Many videos across Yakutia near Olekminsk",
  "No US sensor entry; no stones found","Video only"),
 ("2019 MO","T08","2019 06 22.409050","2019-06-22 21:25:47",9,9,
  "GOES-16 lightning mapper, US sensors (6 kt), infrasound, NEXRAD radar",
  "30-minute ATLAS arc linked after the fact; Pan-STARRS precovery extended it to 2.3 h","Retrospective link"),
 ("2024 UQ","T05","2024 10 22.380923","2024-10-22 10:54:48",7,10,
  "GOES flash, US sensors 0.15 kt at 30N 136W",
  "14-minute ATLAS arc; recognized as an impactor only after the flash","Retrospective link"),
 ("2014 AA","G96","2014 01 01.26257","2014-01-02 03:04:00",9,11,
  "Weak infrasound at three CTBTO stations; no optical or sensor detection",
  "Predicted corridor spanned Central America to East Africa","Infrasound only"),
 ("2026 RW1","G96","2026 09 06.364848","2026-09-06 16:07:00",4,12,
  "None reported as of 2026-09-07; absent from CNEOS fireball database, which lags about three weeks",
  "First Aten; first prior-night precovery (F52) linked while in flight","Unconfirmed"),
 ("2026 JN4","U68","2026 05 15.431912","2026-05-15 13:36:00",9,13,
  "No sensor or camera detection; entered Earth's shadow 20 min before impact",
  "One eyewitness in Darwin with matching time and direction; MPC declined to list","Unconfirmed"),
]
recs=[]
for (obj,code,disc,imp,U,er,e1,e2,tier) in rows:
    m = mpc[obj]
    warn = (datetime.strptime(imp,"%Y-%m-%d %H:%M:%S") - mjd2dt(disc)).total_seconds()/3600
    recs.append(dict(obj=obj,code=code,nsta=m["nsta"],nobs=m["nobs"],U=U,warn=warn,er=er,e1=e1,e2=e2,tier=tier))
# rank-sum: nobs desc, nsta desc, warn desc, U asc (ties share the best rank)
def ranks(key, rev):
    vals = sorted({r[key] for r in recs}, reverse=rev)
    return {r["obj"]: 1 + sum(1 for x in recs if (x[key] > r[key] if rev else x[key] < r[key])) for r in recs}
R = {k: ranks(k, rev) for k, rev in (("nobs",True),("nsta",True),("warn",True),("U",False))}
for r in recs:
    r["parts"] = tuple(R[k][r["obj"]] for k in ("nobs","nsta","warn","U"))
    r["score"] = sum(r["parts"])
recs.sort(key=lambda r: (r["score"], -r["nobs"]))
for i,r in enumerate(recs,1): r["rank"]=i
for r in recs:
    print("%2d %-9s %s sta=%2d obs=%3d U=%d warn=%5.1f parts=%s sum=%2d evrank=%2d" % (r["rank"],r["obj"],r["code"],r["nsta"],r["nobs"],r["U"],r["warn"],r["parts"],r["score"],r["er"]))
retro = {"2019 MO","2024 UQ"}
with open("report/table.md","w") as f:
    f.write("| Rank | Object | Disc. | Tel. | Obs | U | Warning | Confirmation evidence | Evid. rank | Tier |\n")
    f.write("|---:|---|---|---:|---:|---:|---:|---|---:|---|\n")
    for r in recs:
        w = "%.1f h%s" % (r["warn"], "*" if r["obj"] in retro else "")
        f.write("| %d | %s | %s | %d | %d | %d | %s | %s<br>%s | %d | %s |\n" % (r["rank"],r["obj"],r["code"],r["nsta"],r["nobs"],r["U"],w,r["e1"],r["e2"],r["er"],r["tier"]))
json.dump(recs, open("data/ranking.json","w"), indent=1)
