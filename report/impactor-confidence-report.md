---
title: "Asteroids Discovered Before Impact: Confidence Ranking of the 13 Cases"
subtitle: "From 2008 TC3 to 2026 RW1 (CERNQ52)"
date: "2026-09-07, revised 2026-09-10"
---

## Summary

Thirteen asteroids have been observed in space before entering Earth's atmosphere. The newest, 2026 RW1, was posted to the NEO Confirmation Page as CERNQ52 and discovered by the Catalina Sky Survey at Mount Lemmon (G96) on 2026 September 6 at 08:45 UTC. It entered the atmosphere at about 16:07 UTC over the Indian Ocean near 13.8 S, 116.4 E, roughly 750 km northwest of the Western Australian coast, at local midnight. It is the first Aten-class object found before impact, and the first for which a prior-night precovery (Pan-STARRS 2, F52, on September 5) was linked while the object was still in flight.

Starting with 2026 JN4 in May 2026, the Minor Planet Center adopted new wording in its discovery MPECs: it does "not add the object to the list of past impactors" until it receives a report of a ground or air impact. The same wording appears in MPEC 2026-R64 for 2026 RW1. 2026 JN4 still has no independent confirmation. 2026 RW1 acquired one on 2026 September 9, when the Global Fireball Observatory reported a single long-exposure photograph from Broome, Western Australia, 780 km from the predicted entry, showing a faint fireball at the predicted time about one degree above the horizon, with an astrometric line of sight that falls on the JPL Scout impact corridor. As of 2026 September 10 the MPC has not added 2026 RW1 to its list; ESA's NEOCC has.

## Two kinds of confidence

Confidence in a predicted impact combines two separate probabilities.

- **In-flight confidence, P(impact | astrometry).** Did the tracked object hit? This depends on the number of observations, the number of independent telescopes, the length of the arc and the advance notice, and the orbit uncertainty parameter U. Arcs inside Earth's gravity well stiffen quickly, so even short arcs can yield near-certain impact solutions.
- **Post-impact confidence, P(same object | impact evidence).** Is the fireball or meteorite the tracked object? Meteorites with a camera-network trajectory that matches the pre-impact orbit are the gold standard. A calibrated sensor detection (US government satellite sensors, GOES lightning mapper, multi-station infrasound) at the predicted time and place is next. Eyewitness video is strong when it fixes a trajectory and weak when it is a single report.

For 2019 MO and 2024 UQ the second term did all the work: neither was recognized as an impactor until after the fireball was in the satellite record. They are linked impacts rather than predicted ones.

## Ranking table

The table is sorted by in-flight confidence only. The in-flight rank is the sum of four rank positions: number of observations (descending), number of contributing telescopes (descending), advance notice from discovery to impact (descending), and U (ascending), with ties broken by observation count. The "Evid. rank" column preserves the earlier ordering by total evidence, which weights post-impact confirmation heavily.

Column key: **Disc.** is the MPC observatory code of the discovery station. **Tel.** is the number of distinct MPC station codes contributing astrometry. **Obs** is the total observation count in the MPC database, verified through the MPC Explorer observations API on 2026-09-07. **U** is the MPC orbit uncertainty parameter (JPL condition code). **Warning** is discovery observation to impact; an asterisk marks retrospective cases where the impact solution was computed after the event.

| Rank | Object | Disc. | Tel. | Obs | U | Warning | Confirmation evidence | Evid. rank | Tier |
|---:|---|---|---:|---:|---:|---:|---|---:|---|
| 1 | 2008 TC3 | G96 | 29 | 883 | 4 | 20.1 h | Meteosat 8 flash, US sensors (1 kt), infrasound, KLM pilots; pre-impact spectrum and lightcurve<br>600 Almahata Sitta stones, 10.5 kg (ureilite) | 1 | Meteorites |
| 2 | 2023 CX1 | K88 | 22 | 368 | 4 | 6.7 h | FRIPON camera trajectory, thousands of witnesses across France and England<br>Saint-Pierre-le-Viger stones, about 1 kg (L chondrite) | 2 | Meteorites |
| 3 | 2024 RW1 | G96 | 19 | 187 | 5 | 10.9 h | US sensors 0.2 kt at 18.0N 122.9E, matching ESA's 0.19 kt model<br>Videos from Luzon through typhoon cloud; no stones | 5 | Sensor + video |
| 4 | 2024 XA1 | V00 | 15 | 79 | 5 | 10.3 h | Many videos across Yakutia near Olekminsk<br>No US sensor entry; no stones found | 8 | Video only |
| 5 | 2024 BX1 | K88 | 16 | 328 | 5 | 2.7 h | Widely filmed over Berlin and Leipzig; no US sensor entry<br>200+ Ribbeck stones, 1.8 kg (aubrite) | 3 | Meteorites |
| 6 | 2026 RW1 | G96 | 7 | 30 | 4 | 7.4 h | One long-exposure frame from Broome, 780 km away: faint fireball at the predicted time, 1 deg above the horizon, line of sight on the Scout corridor (GFO, 2026-09-09)<br>No CNEOS entry as of 2026-09-10; not yet on the MPC list. First Aten; first prior-night precovery (F52) linked while in flight | 11 | Photo only |
| 7 | 2022 WJ1 | G96 | 10 | 51 | 6 | 3.6 h | All-sky camera trajectory, widespread video from Ontario and four US states<br>Weather radar tracked falling stones into Lake Ontario; none recovered | 6 | Trajectory + radar |
| 8 | 2022 EB5 | K88 | 7 | 177 | 6 | 2.0 h | US sensors 3.8 kt at 70.0N 9.1W; infrasound in Greenland and Norway<br>Possible flash seen from northern Iceland; ESA model only 0.4 kt | 7 | Sensor |
| 9 | 2018 LA | G96 | 4 | 18 | 6 | 8.5 h | US sensors (0.9 kt), many dashcam and security videos in Botswana<br>Motopi Pan stones, Central Kalahari (howardite) | 4 | Meteorites |
| 10 | 2019 MO | T08 | 2 | 7 | 9 | 11.6 h* | GOES-16 lightning mapper, US sensors (6 kt), infrasound, NEXRAD radar<br>30-minute ATLAS arc linked after the fact; Pan-STARRS precovery extended it to 2.3 h | 9 | Retrospective link |
| 11 | 2014 AA | G96 | 1 | 7 | 9 | 20.8 h | Weak infrasound at three CTBTO stations; no optical or sensor detection<br>Predicted corridor spanned Central America to East Africa | 12 | Infrasound only |
| 12 | 2024 UQ | T05 | 2 | 9 | 7 | 1.8 h* | GOES flash, US sensors 0.15 kt at 30N 136W<br>14-minute ATLAS arc; recognized as an impactor only after the flash | 10 | Retrospective link |
| 13 | 2026 JN4 | U68 | 3 | 6 | 9 | 3.2 h | No sensor or camera detection; entered Earth's shadow 20 min before impact<br>One eyewitness in Darwin with matching time and direction; MPC declined to list | 13 | Unconfirmed |

Observation counts are MPC Explorer totals. For 2026 RW1 the Explorer returns 30 observations while MPEC 2026-R64 lists 29 with different per-station counts (G96 5 versus 3, V00 5 versus 4, E10 5 versus 9); the table uses the Explorer count. JPL's Small-Body Database uses fewer in its fits for several objects (2008 TC3: 575 used; 2024 RW1: 76 used, because 92 observations from station D29 are excluded; 2023 CX1: 331; 2024 XA1: 60). The ranking uses the MPC totals.

## Reading the table

**The tiers by evidence.** Four cases have recovered meteorites and are certain: 2008 TC3, 2023 CX1, 2024 BX1, and 2018 LA. Four more have trajectories or calibrated sensor detections at the predicted time and place: 2024 RW1, 2022 WJ1, 2022 EB5, and 2024 XA1. Four rest on a single confirming channel or a retrospective linkage: 2019 MO, 2024 UQ, 2026 RW1, and 2014 AA. One has nothing yet: 2026 JN4.

**The in-flight ordering tells a different story.** By astrometry alone 2026 RW1 rises from 11th to 6th. Thirty observations from seven stations on three continents, a 27-hour arc including the Pan-STARRS 2 precovery pair, and U = 4 tie it with 2008 TC3 and 2023 CX1 for the best-determined orbit in the set. Its P(impact | astrometry) is effectively unity. Conversely 2018 LA drops from 4th to 9th: its 18 observations from four stations were thin, and the meteorites in the Kalahari are what make it certain. 2024 BX1 drops from 3rd to 5th because its 2.7-hour warning was short even though its 328 observations were plentiful.

**Where 2026 RW1 stands.** The second term is thin but no longer empty. The entry was over open ocean at local midnight, at a slow 12 km/s, with an energy near 0.01 to 0.02 kt. Objects that small usually escape the US sensor record: 2022 WJ1, 2023 CX1, 2024 BX1, and 2024 XA1 all have blank sensor entries, and CNEOS still shows nothing for September 6. There is no geostationary lightning mapper over the Indian Ocean, and the Desert Fireball Network cameras in Western Australia were at the edge of their range. What exists is one frame. With five hours' notice, the Global Fireball Observatory team in Perth found the only clear sky within reach on the Broome coast and recruited a local photographer through a Facebook group. He ran 15-second exposures at the northwest horizon. The first candidate was a false lead, 20 minutes late and 45 degrees off in azimuth. A fainter streak at the right time, about a degree above the horizon, gave an astrometric line of sight that lands on the Scout corridor without any fit to the fireball itself. That is a single-station detection, prompted by the prediction rather than blind, with no second camera, sensor, or infrasound channel, so it cannot fix a trajectory or an energy. It ranks just above 2014 AA here because it pins time and direction against a narrow predicted corridor, where 2014 AA's weak infrasound placed a rough location on a corridor spanning half the globe. The two are close, and a published analysis or a sensor detection would settle the order. The MPC had not added 2026 RW1 to its list as of 2026 September 10.

**2026 RW1's two firsts.** Every earlier pre-impact discovery was an Apollo. 2026 RW1 is an Aten with a = 0.94 AU and aphelion at 1.12 AU, so Earth overtook it near aphelion from behind at only 5 km/s. It is also the first case where observations from the previous night, by a different survey, were identified and linked while the object was still inbound. 2019 MO's Pan-STARRS precovery was found after the impact, and the earlier same-night observations of 2024 XA1 and 2026 JN4 by ZTF preceded discovery by only one to two hours.

## What the class tells us

- **The population is a selection effect, not a sample.** Every object was found within roughly a lunar distance, at magnitude 16 to 20, from the night side. Warning time by discovery telescope: the 1.5 m Mount Lemmon reflector gave 3.6 to 21 hours, the 2.3 m Bok 10.3 hours, the 0.6 m Piszkéstető Schmidt 2.0 to 6.7 hours, the 0.5 m ATLAS units 1.8 and 11.6 hours (both retrospective), and the 0.28 m SynTrack 3.2 hours. Sizes have shrunk from 3 to 4 m in 2008 to about 1 m now because the surveys improved, not because the flux changed.
- **The first Aten is what the selection effect predicts.** Night-side discovery of an Aten requires catching it near aphelion, where Earth overtakes it slowly. That is why 2026 RW1 arrived with the lowest relative velocity in the set, the gentlest entry, and the least energy, which in turn is why it is hard to confirm. Slow, low-inclination, near-1 AU orbits dominate the whole list for the same reason: they linger in the detectable volume longest.
- **Orbits are ordinary NEO orbits.** Inclinations run 0.1 to 13 degrees in the JPL solutions (MPEC 2026-J143's six-observation solution gives 10.9 degrees for 2026 JN4 where JPL gives 13.0). Perihelia run 0.59 to 0.94 AU. Nine of 13 have aphelia inside 3 AU, 2024 UQ reaches 3.74 AU, and three (2019 MO, 2022 EB5, 2024 RW1) reach past 4 AU.
- **Compositions are diverse.** The four recovered falls are a ureilite, a howardite, an L chondrite, and an aubrite. Four falls, four classes, two of them achondrites, which make up under a tenth of witnessed falls. Small numbers, but they hint that meter-scale impactors sample the full NEO source mix.
- **Confirmation depends on geography, not on the object.** Every meteorite case fell over land. Every unconfirmed or single-channel case fell over ocean or remote terrain. The two weakest events, four months apart, were both predicted over ocean north and northwest of Australia, beyond camera-network and geostationary lightning-mapper coverage. 2026 RW1's one photograph came from a horizon-grazing view 780 km away, arranged within hours of the prediction, which is the kind of confirmation that geography allows there.
- **We catch a few percent.** The CNEOS fireball database logs 30 to 40 events per year above 0.1 kt. Pre-impact discoveries ran about one per year through 2019 and now run two to four. Nine of the 13 were discovered between September and March, matching long Northern Hemisphere nights and the latitudes of the discovering telescopes.
- **Modeled energies scatter against measured ones.** Both exist for only three objects: 2008 TC3 (1.0 kt measured, 1.1 kt modeled), 2024 RW1 (0.2 versus 0.19), and 2022 EB5 (3.8 versus 0.4). The EB5 case alone is a factor of two in diameter, the limit of what H can deliver for a meter-class object.

The sources disagree on 2026 JN4's entry time. The ESA past-impactors table gives 15:39:28 UTC, with an entry speed of 17.34 km/s, 0.0156 kt, and a diameter of 0.5 to 1.2 m, while the MPC, the International Meteor Organization, and independent computations give 13:36 to 13:44 UTC. The discrepancy is unresolved. ESA lists 2026 JN4 as its twelfth past impactor; the MPC does not list it.

## Sources

- MPEC 2026-R64 (2026 RW1): https://www.minorplanetcenter.net/mpec/K26/K26R64.html
- MPEC 2026-J143 (2026 JN4): https://minorplanetcenter.net/mpec/K26/K26JE3.html
- MPC Explorer observations (verification of counts and station codes): https://data.minorplanetcenter.net/explorer/
- JPL Small-Body Database API (orbits, U): https://ssd-api.jpl.nasa.gov/sbdb.api
- CNEOS fireball database API (US government sensor detections): https://ssd-api.jpl.nasa.gov/fireball.api
- ESA NEOCC past impactors: https://neo.ssa.esa.int/past-impactors
- ESA NEOCC 2026 JN4: https://neo.ssa.esa.int/past-impactors/2026jn4
- Wikipedia, list of predicted asteroid impacts: https://en.wikipedia.org/wiki/List_of_predicted_asteroid_impacts_on_Earth
- Wikipedia object pages: 2014 AA, 2019 MO, 2022 EB5, 2022 WJ1, 2024 RW1, 2024 UQ, 2024 XA1, 2026 JN4, 2026 RW1 (fr)
- The Watchers on 2026 RW1: https://watchers.news/2026/09/07/asteroid-2026-rw1-impacts-earth-over-indian-ocean-september-6-2026-13th-predicted-impactor/
- The Watchers on 2026 JN4: https://watchers.news/2026/05/16/asteroid-2026-jn4-impacts-earth-arafura-sea-may-15-2026/
- EarthSky on 2026 RW1: https://earthsky.org/space/small-asteroid-impact-australia-sep-6-2026/
- Global Fireball Observatory, "2026 RW1 = CERNQ52: impact confirmed!" (H. Devillepoix; the page header and URL are dated June 9, evidently a slip for September 9, and the page says last updated 2026-09-09 AWST): https://gfo.rocks/blog/2026/06/09/2026-RW1_impact-confirmation.html
- ESA NEOCC 2026 RW1: https://neo.ssa.esa.int/past-impactors/2026rw1
