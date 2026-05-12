# PIT SOUNDINGS (Pittsburgh, Pennsulvania)
#%%
#5/30 at 00z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir
from metpy.calc import mixed_layer, parcel_profile #for MLCAPE


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 30, 00)
station = 'PIT'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');

plt.savefig('PIT_Sounding_May30_00z.png')
plt.show()
#%% 
#5/30 at 12z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 30, 12)
station = 'PIT'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');

plt.savefig('PIT_Sounding_May30_12z.png')
plt.show()
#%%
#5/31 at 00z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 31, 00)
station = 'PIT'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');

plt.savefig('PIT_Sounding_May31_00z.png')
plt.show()
#%%
#5/31 at 12z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 31, 12)
station = 'PIT'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');

plt.savefig('PIT_Sounding_May31_12z.png')
plt.show()
#%%
#
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 6, 1, 00)
station = 'PIT'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');

plt.savefig('PIT_Sounding_June1_00z.png')
plt.show()
#%%
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 6, 1, 12)
station = 'PIT'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');

plt.savefig('PIT_Sounding_June1_12z.png')
plt.show()
#%% 
# BUF SOUNDINGS (Buffalo, New York)
#%%
#5/30 at 00z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 30, 00)
station = 'BUF'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('BUF_Sounding_May30_00z.png')
plt.show()
#%%
#5/30 at 12z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 30, 12)
station = 'BUF'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('BUF_Sounding_May30_12z.png')
plt.show()
#%%
#5/31 at 00z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 31, 00)
station = 'BUF'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('BUF_Sounding_May31_00z.png')
plt.show()
#%%
#5/31 at 12z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 31, 12)
station = 'BUF'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('BUF_Sounding_May31_12z.png')
plt.show()
#%%
#6/1 at 00z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 6, 1, 00)
station = 'BUF'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('BUF_Sounding_June1_00z.png')
plt.show()
#%%
#6/1 at 12z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 6, 1, 12)
station = 'BUF'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('BUF_Sounding_June1_12z.png')
plt.show()
#%% 
# HTS SOUNDINGS (Huntington, West Virgina)
#%%
#5/30 at 00z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 30, 00)
station = 'HTS'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('HTS_Sounding_May30_00z.png')
plt.show()
#%%
#5/30 at 12z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 30, 12)
station = 'HTS'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('HTS_Sounding_May30_12z.png')
plt.show()
#%%
#5/31 at 00z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 31, 00)
station = 'HTS'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('HTS_Sounding_May31_00z.png')
plt.show()
#%%
#5/31 at 12z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 31, 12)
station = 'HTS'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('HTS_Sounding_May31_12z.png')
plt.show()
#%%
#6/1 at 00z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 6, 1, 00)
station = 'HTS'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('HTS_Sounding_June1_00z.png')
plt.show()
#%%
#6/1 at 12z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 6, 1, 12)
station = 'HTS'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('HTS_Sounding_June_12z.png')
plt.show()
#%% 
# DAY SOUNDINGS (Dayton, Ohio) NOTE: no sounding for 5/31 at 00z
#%%
#5/30 at 00z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 30, 00)
station = 'DAY'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('DAY_Sounding_May30_00z.png')
plt.show()
#%%
#5/30 at 12z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 30, 12)
station = 'DAY'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('DAY_Sounding_May30_12z.png')
plt.show()
#%%
#5/31 at 12z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 5, 31, 12)
station = 'DAY'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('DAY_Sounding_May31_12z.png')
plt.show()

#%%
#6/1 at 00z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 6, 1, 00)
station = 'DAY'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('DAY_Sounding_June1_00z.png')
plt.show()

#%%
#6/1 at 12z
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skew-T Analysis¶ from Unidata Example
Classic skew-T/log-p plot using data from University of Wyoming.

This example uses example data from the University of Wyoming sounding archive for 12 UTC 31 October 2016 for Minneapolis, MN (MPX) and uses MetPy to plot the classic skew-T with Temperature, Dewpoint, and wind barbs.
"""

from datetime import datetime

import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Set time using a datetime object and station as variables
dt = datetime(1985, 6, 1, 12)
station = 'DAY'

#Grab Remote Data
#This requires an internet connection to access the sounding data from a 
#remote server at the University of Wyoming.

# Read remote sounding data based on time (dt) and station
df = WyomingUpperAir.request_data(dt, station)

# Create dictionary of united arrays
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot
#The code below makes a basic skew-T plot using the MetPy plot module that 
#contains a SkewT class.

# Change default to be better for skew-T
fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

#set SBCAPE
sfc_temp = T[0]
sfc_dewpoint = Td[0]
sbcape_prof = parcel_profile(p, sfc_temp, sfc_dewpoint)
skew.plot(p, sbcape_prof, color='blue', linewidth=2)

#set MLCAPE 
ml_temp, ml_dewpoint = mixed_layer(p, T, Td, depth=100 * units.hPa)
ml_parcel_prof = parcel_profile(p, ml_temp, ml_dewpoint)
skew.plot(p, ml_parcel_prof, color='orange', linewidth=2)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio=None,pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');
plt.savefig('DAY_Sounding_June1_12z.png')
plt.show()
#%% GIF PIT Sounding
from PIL import Image

i1 = Image.open('PIT_Sounding_May31_12z.png')
i2 = Image.open('PIT_Sounding_June1_00z.png')
i3 = Image.open('PIT_Sounding_June1_12z.png')
i1.save('PIT_Sounding_May31_June1.gif',
        save_all=True,
        append_images=[i2, i3],
        duration=4000,
        loop=0)