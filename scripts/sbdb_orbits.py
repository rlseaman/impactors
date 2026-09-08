# Query the JPL Small-Body Database for orbits, observation counts, and condition code (U).
import sys, json, urllib.request
objs = ["2008 TC3","2014 AA","2018 LA","2019 MO","2022 EB5","2022 WJ1","2023 CX1","2024 BX1","2024 RW1","2024 UQ","2024 XA1","2026 JN4","2026 RW1"]
for o in objs:
    url = "https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=" + o.replace(" ", "%20") + "&phys-par=true"
    try:
        j = json.load(urllib.request.urlopen(url, timeout=60))
    except Exception as e:
        print(o, "ERR", e); continue
    if "object" not in j:
        print(o, "NOT FOUND", j.get("message")); continue
    ob = j["object"]; orb = j["orbit"]
    el = {e["name"]: e["value"] for e in orb["elements"]}
    H = [p["value"] for p in j.get("phys_par", []) if p["name"] == "H"]
    print("%-9s class=%s nobs=%4s arc=%sd first=%s last=%s a=%.3f e=%.3f i=%.2f q=%.3f Q=%.3f H=%s cond=%s" % (
        o, ob["orbit_class"]["code"], orb["n_obs_used"], orb["data_arc"], orb["first_obs"], orb["last_obs"],
        float(el["a"]), float(el["e"]), float(el["i"]), float(el["q"]), float(el["ad"]), H[0] if H else "?", orb.get("condition_code")))
