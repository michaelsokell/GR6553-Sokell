import matplotlib.pyplot as plt
import numpy as np
import pygrib
import cartopy 
import cartopy.feature as cfeature
import cartopy.crs as ccrs 

#MAY 30, 1985
#%% 500 Relative Vorticity 00z
ERA5_05_30=pygrib.open('19850530') #ERA5 May 30, 1985

GeoHeight_500=ERA5_05_30.select(name='Geopotential', level=500, validityTime=0)[0]
GeoHeight_500_data=GeoHeight_500['values']
GeoHeight_500_dm=GeoHeight_500_data/10

#500 Relative Vorticity
RV_500=ERA5_05_30.select(name='Vorticity (relative)', level=500, validityTime=0)[0]
RV_500_data=RV_500['values']

lats,lons=GeoHeight_500.latlons() 

fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120., -75., 21., 55.], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True

bounds=[-4e-4, -3e-4, -2e-4, -1e-4, -5e-5, 0, 5e-5, 1e-4, 2e-4, 3e-4, 4e-4]
  
ca=ax.contourf(lons,lats,RV_500_data,levels=bounds,cmap = plt.cm.RdBu_r, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('s^-1')

#500 geoheight
ax.contour(lons, lats, GeoHeight_500_dm, colors='black',linewidths=1,transform=ccrs.PlateCarree())


plt.title('May 30, 1985 00z 500 mb Relative Vorticity (s^-1)')

plt.savefig('500mb_Relative_Vorticity_May30_00z.png')
plt.show()
#%% 500 Relative Vorticity 06z
ERA5_05_30=pygrib.open('19850530') #ERA5 May 30, 1985

GeoHeight_500=ERA5_05_30.select(name='Geopotential', level=500, validityTime=600)[0]
GeoHeight_500_data=GeoHeight_500['values']
GeoHeight_500_dm=GeoHeight_500_data/10

#500 Relative Vorticity
RV_500=ERA5_05_30.select(name='Vorticity (relative)', level=500, validityTime=600)[0]
RV_500_data=RV_500['values']

lats,lons=GeoHeight_500.latlons() 

fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120., -75., 21., 55.], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True

bounds=[-4e-4, -3e-4, -2e-4, -1e-4, -5e-5, 0, 5e-5, 1e-4, 2e-4, 3e-4, 4e-4]
  
ca=ax.contourf(lons,lats,RV_500_data,levels=bounds,cmap = plt.cm.RdBu_r, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('s^-1')

#500 geoheight
ax.contour(lons, lats, GeoHeight_500_dm, colors='black',linewidths=1,transform=ccrs.PlateCarree())


plt.title('May 30, 1985 06z 500 mb Relative Vorticity (s^-1)')

plt.savefig('500mb_Relative_Vorticity_May30_06z.png')
plt.show()
#%% 500 Relative Vorticity 12z
ERA5_05_30=pygrib.open('19850530') #ERA5 May 30, 1985

GeoHeight_500=ERA5_05_30.select(name='Geopotential', level=500, validityTime=1200)[0]
GeoHeight_500_data=GeoHeight_500['values']
GeoHeight_500_dm=GeoHeight_500_data/10

#500 Relative Vorticity
RV_500=ERA5_05_30.select(name='Vorticity (relative)', level=500, validityTime=1200)[0]
RV_500_data=RV_500['values']

lats,lons=GeoHeight_500.latlons() 

fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120., -75., 21., 55.], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True

bounds=[-4e-4, -3e-4, -2e-4, -1e-4, -5e-5, 0, 5e-5, 1e-4, 2e-4, 3e-4, 4e-4]
  
ca=ax.contourf(lons,lats,RV_500_data,levels=bounds,cmap = plt.cm.RdBu_r, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('s^-1')

#500 geoheight
ax.contour(lons, lats, GeoHeight_500_dm, colors='black',linewidths=1,transform=ccrs.PlateCarree())


plt.title('May 30, 1985 12z 500 mb Relative Vorticity (s^-1)')

plt.savefig('500mb_Relative_Vorticity_May30_12z.png')
plt.show()
#%% 500 Relative Vorticity 18z
ERA5_05_30=pygrib.open('19850530') #ERA5 May 30, 1985

GeoHeight_500=ERA5_05_30.select(name='Geopotential', level=500, validityTime=1800)[0]
GeoHeight_500_data=GeoHeight_500['values']
GeoHeight_500_dm=GeoHeight_500_data/10

#500 Relative Vorticity
RV_500=ERA5_05_30.select(name='Vorticity (relative)', level=500, validityTime=1800)[0]
RV_500_data=RV_500['values']

lats,lons=GeoHeight_500.latlons() 

fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120., -75., 21., 55.], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True

bounds=[-4e-4, -3e-4, -2e-4, -1e-4, -5e-5, 0, 5e-5, 1e-4, 2e-4, 3e-4, 4e-4]
  
ca=ax.contourf(lons,lats,RV_500_data,levels=bounds,cmap = plt.cm.RdBu_r, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('s^-1')

#500 geoheight
ax.contour(lons, lats, GeoHeight_500_dm, colors='black',linewidths=1,transform=ccrs.PlateCarree())


plt.title('May 30, 1985 18z 500 mb Relative Vorticity (s^-1)')

plt.savefig('500mb_Relative_Vorticity_May30_18z.png')
plt.show()

#%% MAY 31, 1985
#%% 500 Relative Vorticity 00z
ERA5_05_31=pygrib.open('19850531') #ERA5 May 30, 1985

GeoHeight_500=ERA5_05_31.select(name='Geopotential', level=500, validityTime=0)[0]
GeoHeight_500_data=GeoHeight_500['values']
GeoHeight_500_dm=GeoHeight_500_data/10

#500 Relative Vorticity
RV_500=ERA5_05_31.select(name='Vorticity (relative)', level=500, validityTime=0)[0]
RV_500_data=RV_500['values']

lats,lons=GeoHeight_500.latlons() 

fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120., -75., 21., 55.], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True

bounds=[-4e-4, -3e-4, -2e-4, -1e-4, -5e-5, 0, 5e-5, 1e-4, 2e-4, 3e-4, 4e-4]
  
ca=ax.contourf(lons,lats,RV_500_data,levels=bounds,cmap = plt.cm.RdBu_r, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('s^-1')

#500 geoheight
ax.contour(lons, lats, GeoHeight_500_dm, colors='black',linewidths=1,transform=ccrs.PlateCarree())


plt.title('May 31, 1985 00z 500 mb Relative Vorticity (s^-1)')

plt.savefig('500mb_Relative_Vorticity_May31_00z.png')
plt.show()
#%% 500 Relative Vorticity 06z
ERA5_05_31=pygrib.open('19850531') #ERA5 May 30, 1985

GeoHeight_500=ERA5_05_31.select(name='Geopotential', level=500, validityTime=600)[0]
GeoHeight_500_data=GeoHeight_500['values']
GeoHeight_500_dm=GeoHeight_500_data/10

#500 Relative Vorticity
RV_500=ERA5_05_31.select(name='Vorticity (relative)', level=500, validityTime=600)[0]
RV_500_data=RV_500['values']

lats,lons=GeoHeight_500.latlons() 

fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120., -75., 21., 55.], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True

bounds=[-4e-4, -3e-4, -2e-4, -1e-4, -5e-5, 0, 5e-5, 1e-4, 2e-4, 3e-4, 4e-4]
  
ca=ax.contourf(lons,lats,RV_500_data,levels=bounds,cmap = plt.cm.RdBu_r, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('s^-1')

#500 geoheight
ax.contour(lons, lats, GeoHeight_500_dm, colors='black',linewidths=1,transform=ccrs.PlateCarree())


plt.title('May 31, 1985 06z 500 mb Relative Vorticity (s^-1)')

plt.savefig('500mb_Relative_Vorticity_May31_06z.png')
plt.show()
#%% 500 Relative Vorticity 12z
ERA5_05_31=pygrib.open('19850531') #ERA5 May 30, 1985

GeoHeight_500=ERA5_05_31.select(name='Geopotential', level=500, validityTime=1200)[0]
GeoHeight_500_data=GeoHeight_500['values']
GeoHeight_500_dm=GeoHeight_500_data/10

#500 Relative Vorticity
RV_500=ERA5_05_31.select(name='Vorticity (relative)', level=500, validityTime=1200)[0]
RV_500_data=RV_500['values']

lats,lons=GeoHeight_500.latlons() 

fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120., -75., 21., 55.], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True

bounds=[-4e-4, -3e-4, -2e-4, -1e-4, -5e-5, 0, 5e-5, 1e-4, 2e-4, 3e-4, 4e-4]
  
ca=ax.contourf(lons,lats,RV_500_data,levels=bounds,cmap = plt.cm.RdBu_r, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('s^-1')

#500 geoheight
ax.contour(lons, lats, GeoHeight_500_dm, colors='black',linewidths=1,transform=ccrs.PlateCarree())


plt.title('May 31, 1985 12z 500 mb Relative Vorticity (s^-1)')

plt.savefig('500mb_Relative_Vorticity_May31_12z.png')
plt.show()
#%% 500 Relative Vorticity 18z
ERA5_05_31=pygrib.open('19850531') #ERA5 May 30, 1985

GeoHeight_500=ERA5_05_31.select(name='Geopotential', level=500, validityTime=1800)[0]
GeoHeight_500_data=GeoHeight_500['values']
GeoHeight_500_dm=GeoHeight_500_data/10

#500 Relative Vorticity
RV_500=ERA5_05_31.select(name='Vorticity (relative)', level=500, validityTime=1800)[0]
RV_500_data=RV_500['values']

lats,lons=GeoHeight_500.latlons() 

fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120., -75., 21., 55.], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True

bounds=[-4e-4, -3e-4, -2e-4, -1e-4, -5e-5, 0, 5e-5, 1e-4, 2e-4, 3e-4, 4e-4]
  
ca=ax.contourf(lons,lats,RV_500_data,levels=bounds,cmap = plt.cm.RdBu_r, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('s^-1')

#500 geoheight
ax.contour(lons, lats, GeoHeight_500_dm, colors='black',linewidths=1,transform=ccrs.PlateCarree())


plt.title('May 31, 1985 18z 500 mb Relative Vorticity (s^-1)')

plt.savefig('500mb_Relative_Vorticity_May31_18z.png')
plt.show()
#%% JUNE 1, 1985
#%% 500 Relative Vorticity 00z
ERA5_06_01=pygrib.open('19850601') #ERA5 June 1, 1985

GeoHeight_500=ERA5_06_01.select(name='Geopotential', level=500, validityTime=0)[0]
GeoHeight_500_data=GeoHeight_500['values']
GeoHeight_500_dm=GeoHeight_500_data/10

#500 Relative Vorticity
RV_500=ERA5_06_01.select(name='Vorticity (relative)', level=500, validityTime=0)[0]
RV_500_data=RV_500['values']

lats,lons=GeoHeight_500.latlons() 

fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120., -75., 21., 55.], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True

bounds=[-4e-4, -3e-4, -2e-4, -1e-4, -5e-5, 0, 5e-5, 1e-4, 2e-4, 3e-4, 4e-4]
  
ca=ax.contourf(lons,lats,RV_500_data,levels=bounds,cmap = plt.cm.RdBu_r, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('s^-1')

#500 geoheight
ax.contour(lons, lats, GeoHeight_500_dm, colors='black',linewidths=1,transform=ccrs.PlateCarree())


plt.title('June 1, 1985 00z 500 mb Relative Vorticity (s^-1)')

plt.savefig('500mb_Relative_Vorticity_June1_00z.png')
plt.show()
#%% 500 Relative Vorticity 06z
ERA5_06_01=pygrib.open('19850601') #ERA5 June 1, 1985

GeoHeight_500=ERA5_06_01.select(name='Geopotential', level=500, validityTime=600)[0]
GeoHeight_500_data=GeoHeight_500['values']
GeoHeight_500_dm=GeoHeight_500_data/10

#500 Relative Vorticity
RV_500=ERA5_06_01.select(name='Vorticity (relative)', level=500, validityTime=600)[0]
RV_500_data=RV_500['values']

lats,lons=GeoHeight_500.latlons() 

fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120., -75., 21., 55.], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True

bounds=[-4e-4, -3e-4, -2e-4, -1e-4, -5e-5, 0, 5e-5, 1e-4, 2e-4, 3e-4, 4e-4]
  
ca=ax.contourf(lons,lats,RV_500_data,levels=bounds,cmap = plt.cm.RdBu_r, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('s^-1')

#500 geoheight
ax.contour(lons, lats, GeoHeight_500_dm, colors='black',linewidths=1,transform=ccrs.PlateCarree())


plt.title('June 1, 1985 06z 500 mb Relative Vorticity (s^-1)')

plt.savefig('500mb_Relative_Vorticity_June1_06z.png')
plt.show()
#%% 500 Relative Vorticity 18z
ERA5_06_01=pygrib.open('19850601') #ERA5 June 1, 1985

GeoHeight_500=ERA5_06_01.select(name='Geopotential', level=500, validityTime=1800)[0]
GeoHeight_500_data=GeoHeight_500['values']
GeoHeight_500_dm=GeoHeight_500_data/10

#500 Relative Vorticity
RV_500=ERA5_06_01.select(name='Vorticity (relative)', level=500, validityTime=1800)[0]
RV_500_data=RV_500['values']

lats,lons=GeoHeight_500.latlons() 

fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120., -75., 21., 55.], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True

bounds=[-4e-4, -3e-4, -2e-4, -1e-4, -5e-5, 0, 5e-5, 1e-4, 2e-4, 3e-4, 4e-4]
  
ca=ax.contourf(lons,lats,RV_500_data,levels=bounds,cmap = plt.cm.RdBu_r, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('s^-1')

#500 geoheight
ax.contour(lons, lats, GeoHeight_500_dm, colors='black',linewidths=1,transform=ccrs.PlateCarree())


plt.title('June 1, 1985 18z 500 mb Relative Vorticity (s^-1)')

plt.savefig('500mb_Relative_Vorticity_June1_18z.png')
plt.show()
#%% GIF May 30
from PIL import Image

i1 = Image.open('500mb_Relative_Vorticity_May30_00z.png')
i2 = Image.open('500mb_Relative_Vorticity_May30_06z.png')
i3 = Image.open('500mb_Relative_Vorticity_May30_12z.png')
i4 = Image.open('500mb_Relative_Vorticity_May30_18z.png')
i1.save('500_RV_May30.gif',
        save_all=True,
        append_images=[i2, i3, i4],
        duration=1400,
        loop=0)
#%% GIF May 31 
from PIL import Image

i1 = Image.open('500mb_Relative_Vorticity_May31_00z.png')
i2 = Image.open('500mb_Relative_Vorticity_May31_06z.png')
i3 = Image.open('500mb_Relative_Vorticity_May31_12z.png')
i4 = Image.open('500mb_Relative_Vorticity_May31_18z.png')
i1.save('500_RV_May31.gif',
        save_all=True,
        append_images=[i2, i3, i4],
        duration=1400,
        loop=0)
#%% GIF June 1
from PIL import Image

i1 = Image.open('500mb_Relative_Vorticity_June1_00z.png')
i2 = Image.open('500mb_Relative_Vorticity_June1_06z.png')
i3 = Image.open('500mb_Relative_Vorticity_June1_18z.png')
i1.save('500_RV_June1.gif',
        save_all=True,
        append_images=[i2, i3],
        duration=1400,
        loop=0)