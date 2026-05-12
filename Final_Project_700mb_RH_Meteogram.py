import pygrib
import numpy as np
import matplotlib.pyplot as plt

lat0 = 41.20028
lon0 = -80.49583
#%% Wheatland, PA F5 6:30-7:45
#%% May 30 
may30 = pygrib.open("19850530")

#timescale
hours = {0: "00Z", 600: "06Z", 1200: "12Z", 1800: "18Z"}

#keeping RH values found for each hour
rh_point = {}

#Find RH value for each hour
for msg in may30:
    if msg.name == "Relative humidity" and msg.level == 700:
        if msg.dataTime in hours:

            # Get lat/lon grid
            lats, lons = msg.latlons()

            # Nearest grid point
            dist = (lats - lat0)**2 + (lons - lon0)**2
            iy, ix = np.unravel_index(dist.argmin(), dist.shape)

            # Store RH value
            rh_point[hours[msg.dataTime]] = msg.values[iy, ix]

#meteogram
times = ["00Z", "06Z", "12Z", "18Z"]
values = [rh_point[t] for t in times]

plt.figure(figsize=(10,5))
plt.plot(times, values, marker="o", color="green", linewidth=2)

plt.title("5/30 700‑mb Relative Humidity Meteogram for Wheatland, PA")
plt.ylabel("Relative Humidity (%)")
plt.grid(True, linestyle="--", alpha=0.5)

plt.ylim(0, 100)
plt.yticks(np.arange(0, 101, 20))

plt.savefig('700mb_Relative_Humidity_May30.png')
plt.show()
#%% May 31
may31 = pygrib.open("19850531")

#timescale
hours = {0: "00Z", 600: "06Z", 1200: "12Z", 1800: "18Z"}

#keeping RH values found for each hour
rh_point = {}

#Find RH value for each hour
for msg in may31:
    if msg.name == "Relative humidity" and msg.level == 700:
        if msg.dataTime in hours:

            # Get lat/lon grid
            lats, lons = msg.latlons()

            # Nearest grid point
            dist = (lats - lat0)**2 + (lons - lon0)**2
            iy, ix = np.unravel_index(dist.argmin(), dist.shape)

            # Store RH value
            rh_point[hours[msg.dataTime]] = msg.values[iy, ix]

#meteogram
times = ["00Z", "06Z", "12Z", "18Z"]
values = [rh_point[t] for t in times]

plt.figure(figsize=(10,5))
plt.plot(times, values, marker="o", color="green", linewidth=2)

plt.title("5/31 700‑mb Relative Humidity Meteogram for Wheatland, PA")
plt.ylabel("Relative Humidity (%)")
plt.grid(True, linestyle="--", alpha=0.5)

plt.ylim(0, 100)
plt.yticks(np.arange(0, 101, 20))

plt.savefig('700mb_Relative_Humidity_May31.png')
plt.show()
#%% June 1
june1 = pygrib.open("19850601")

#timescale
hours = {0: "00Z", 600: "06Z", 1200: "12Z", 1800: "18Z"}

#keeping RH values found for each hour
rh_point = {}

#Find RH value for each hour
for msg in june1:
    if msg.name == "Relative humidity" and msg.level == 700:
        if msg.dataTime in hours:

            # Get lat/lon grid
            lats, lons = msg.latlons()

            # Nearest grid point
            dist = (lats - lat0)**2 + (lons - lon0)**2
            iy, ix = np.unravel_index(dist.argmin(), dist.shape)

            # Store RH value
            rh_point[hours[msg.dataTime]] = msg.values[iy, ix]

#meteogram
times = ["00Z", "06Z", "12Z", "18Z"]
values = [rh_point[t] for t in times]

plt.figure(figsize=(10,5))
plt.plot(times, values, marker="o", color="green", linewidth=2)

plt.title("6/1 700‑mb Relative Humidity Meteogram for Wheatland, PA")
plt.ylabel("Relative Humidity (%)")
plt.grid(True, linestyle="--", alpha=0.5)

plt.ylim(0, 100)
plt.yticks(np.arange(0, 101, 20))

plt.savefig('700mb_Relative_Humidity_June1.png')
plt.show()