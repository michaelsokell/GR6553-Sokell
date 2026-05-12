import matplotlib.pyplot as plt
import numpy as np
import pygrib
import cartopy 
import cartopy.feature as cfeature
import cartopy.crs as ccrs 

#MAY 31, 1985
#%% 1000 hpa 00z
ERA5_05_31=pygrib.open('May31SFC.grib') #ERA5 May 31, 1985

GeoHeight_1000=ERA5_05_31.select(name='Geopotential', level=1000, validityTime=0)[0]
GeoHeight_1000_data=GeoHeight_1000['values']
GeoHeight_1000_dm=GeoHeight_1000_data/10

#1000 Winds (U), 
uwind1000=ERA5_05_31.select(name='U component of wind', level=1000, validityTime=0)[0]
uwind1000_data=uwind1000['values']
uwind1000_kt=uwind1000_data*1.94

#1000 Winds (V)
vwind1000=ERA5_05_31.select(name='V component of wind', level=1000, validityTime=0)[0] 
vwind1000_data=vwind1000['values']
vwind1000_kt=vwind1000_data*1.94


#1000 Temperature
temp1000=ERA5_05_31.select(name='Temperature', level=1000, validityTime=0)[0] 
temp1000_data=temp1000['values']
temp1000_F=(temp1000_data-273.15)*(9/5)+32

lats,lons=GeoHeight_1000.latlons() 


fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-100.,-70.,35.,50.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='black')
ax.add_feature(cfeature.BORDERS, edgecolor='black')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,temp1000_F,levels=bounds,cmap=plt.cm.nipy_spectral, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('Fahrenheit')



#windbarbs
ax.barbs(lons[::5,::5],lats[::5,::5],uwind1000_kt[::5,::5],vwind1000_kt[::5,::5],color='black',transform=ccrs.PlateCarree())

#1000 geoheight
ax.contour(lons,lats,GeoHeight_1000_dm,np.arange(np.min(GeoHeight_1000_dm),np.max(GeoHeight_1000_dm),15),linewidths=1.5,colors="black",transform=ccrs.PlateCarree())


plt.title('May 31, 1985 00z 1000 mb Heights (dm) / Temperature (F)')

plt.savefig('1000mb_May31_00z.png')
plt.show()
#%% 1000 hpa 06z
ERA5_05_31=pygrib.open('May31SFC.grib') #ERA5 May 31, 1985

GeoHeight_1000=ERA5_05_31.select(name='Geopotential', level=1000, validityTime=600)[0]
GeoHeight_1000_data=GeoHeight_1000['values']
GeoHeight_1000_dm=GeoHeight_1000_data/10

#1000 Winds (U), 
uwind1000=ERA5_05_31.select(name='U component of wind', level=1000, validityTime=600)[0]
uwind1000_data=uwind1000['values']
uwind1000_kt=uwind1000_data*1.94

#1000 Winds (V)
vwind1000=ERA5_05_31.select(name='V component of wind', level=1000, validityTime=600)[0] 
vwind1000_data=vwind1000['values']
vwind1000_kt=vwind1000_data*1.94


#1000 Temperature
temp1000=ERA5_05_31.select(name='Temperature', level=1000, validityTime=600)[0] 
temp1000_data=temp1000['values']
temp1000_F=(temp1000_data-273.15)*(9/5)+32

lats,lons=GeoHeight_1000.latlons() 


fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-100.,-70.,35.,50.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='black')
ax.add_feature(cfeature.BORDERS, edgecolor='black')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,temp1000_F,levels=bounds,cmap=plt.cm.nipy_spectral, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('Fahrenheit')



#windbarbs
ax.barbs(lons[::5,::5],lats[::5,::5],uwind1000_kt[::5,::5],vwind1000_kt[::5,::5],color='black',transform=ccrs.PlateCarree())

#1000 geoheight
ax.contour(lons,lats,GeoHeight_1000_dm,np.arange(np.min(GeoHeight_1000_dm),np.max(GeoHeight_1000_dm),15),linewidths=1.5,colors="black",transform=ccrs.PlateCarree())

plt.title('May 31, 1985 06z 1000 mb Heights (dm) / Temperature (F)')

plt.savefig('1000mb_May31_06z.png')
plt.show()
#%% 1000 hpa 12z
ERA5_05_31=pygrib.open('May31SFC.grib') #ERA5 May 31, 1985

GeoHeight_1000=ERA5_05_31.select(name='Geopotential', level=1000, validityTime=1200)[0]
GeoHeight_1000_data=GeoHeight_1000['values']
GeoHeight_1000_dm=GeoHeight_1000_data/10

#1000 Winds (U), 
uwind1000=ERA5_05_31.select(name='U component of wind', level=1000, validityTime=1200)[0]
uwind1000_data=uwind1000['values']
uwind1000_kt=uwind1000_data*1.94

#1000 Winds (V)
vwind1000=ERA5_05_31.select(name='V component of wind', level=1000, validityTime=1200)[0] 
vwind1000_data=vwind1000['values']
vwind1000_kt=vwind1000_data*1.94


#1000 Temperature
temp1000=ERA5_05_31.select(name='Temperature', level=1000, validityTime=1200)[0] 
temp1000_data=temp1000['values']
temp1000_F=(temp1000_data-273.15)*(9/5)+32

lats,lons=GeoHeight_1000.latlons() 


fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-100.,-70.,35.,50.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='black')
ax.add_feature(cfeature.BORDERS, edgecolor='black')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,temp1000_F,levels=bounds,cmap=plt.cm.nipy_spectral, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('Fahrenheit')



#windbarbs
ax.barbs(lons[::5,::5],lats[::5,::5],uwind1000_kt[::5,::5],vwind1000_kt[::5,::5],color='black',transform=ccrs.PlateCarree())

#1000 geoheight
ax.contour(lons,lats,GeoHeight_1000_dm,np.arange(np.min(GeoHeight_1000_dm),np.max(GeoHeight_1000_dm),15),linewidths=1.5,colors="black",transform=ccrs.PlateCarree())

plt.title('May 31, 1985 12z 1000 mb Heights (dm) / Temperature (F)')

plt.savefig('1000mb_May31_12z.png')
plt.show()
#%% 1000 hpa 18z
ERA5_05_31=pygrib.open('May31SFC.grib') #ERA5 May 31, 1985

GeoHeight_1000=ERA5_05_31.select(name='Geopotential', level=1000, validityTime=1800)[0]
GeoHeight_1000_data=GeoHeight_1000['values']
GeoHeight_1000_dm=GeoHeight_1000_data/10

#1000 Winds (U), 
uwind1000=ERA5_05_31.select(name='U component of wind', level=1000, validityTime=1800)[0]
uwind1000_data=uwind1000['values']
uwind1000_kt=uwind1000_data*1.94

#1000 Winds (V)
vwind1000=ERA5_05_31.select(name='V component of wind', level=1000, validityTime=1800)[0] 
vwind1000_data=vwind1000['values']
vwind1000_kt=vwind1000_data*1.94


#1000 Temperature
temp1000=ERA5_05_31.select(name='Temperature', level=1000, validityTime=1800)[0] 
temp1000_data=temp1000['values']
temp1000_F=(temp1000_data-273.15)*(9/5)+32

lats,lons=GeoHeight_1000.latlons() 


fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-100.,-70.,35.,50.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='black')
ax.add_feature(cfeature.BORDERS, edgecolor='black')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,temp1000_F,levels=bounds,cmap=plt.cm.nipy_spectral, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('Fahrenheit')



#windbarbs
ax.barbs(lons[::5,::5],lats[::5,::5],uwind1000_kt[::5,::5],vwind1000_kt[::5,::5],color='black',transform=ccrs.PlateCarree())

#1000 geoheight
ax.contour(lons,lats,GeoHeight_1000_dm,np.arange(np.min(GeoHeight_1000_dm),np.max(GeoHeight_1000_dm),15),linewidths=1.5,colors="black",transform=ccrs.PlateCarree())

plt.title('May 31, 1985 18z 1000 mb Heights (dm) / Temperature (F)')

plt.savefig('1000mb_May31_18z.png')
plt.show()
#%%MJUNE 1, 1985
#%% 1000 hpa 00z
ERA5_06_01=pygrib.open('June1SFC.grib') #ERA5 June 1, 1985

GeoHeight_1000=ERA5_06_01.select(name='Geopotential', level=1000, validityTime=0)[0]
GeoHeight_1000_data=GeoHeight_1000['values']
GeoHeight_1000_dm=GeoHeight_1000_data/10

#1000 Winds (U), 
uwind1000=ERA5_06_01.select(name='U component of wind', level=1000, validityTime=0)[0]
uwind1000_data=uwind1000['values']
uwind1000_kt=uwind1000_data*1.94

#1000 Winds (V)
vwind1000=ERA5_06_01.select(name='V component of wind', level=1000, validityTime=0)[0] 
vwind1000_data=vwind1000['values']
vwind1000_kt=vwind1000_data*1.94


#1000 Temperature
temp1000=ERA5_06_01.select(name='Temperature', level=1000, validityTime=0)[0] 
temp1000_data=temp1000['values']
temp1000_F=(temp1000_data-273.15)*(9/5)+32

lats,lons=GeoHeight_1000.latlons() 


fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-100.,-70.,35.,50.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='black')
ax.add_feature(cfeature.BORDERS, edgecolor='black')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,temp1000_F,levels=bounds,cmap=plt.cm.nipy_spectral, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('Fahrenheit')



#windbarbs
ax.barbs(lons[::5,::5],lats[::5,::5],uwind1000_kt[::5,::5],vwind1000_kt[::5,::5],color='black',transform=ccrs.PlateCarree())

#1000 geoheight
ax.contour(lons,lats,GeoHeight_1000_dm,np.arange(np.min(GeoHeight_1000_dm),np.max(GeoHeight_1000_dm),15),linewidths=1.5,colors="black",transform=ccrs.PlateCarree())

plt.title('June 1, 1985 00z 1000 mb Heights (dm) / Temperature (F)')

plt.savefig('1000mb_June1_00z.png')
plt.show()
#%% 1000 hpa 06z
ERA5_06_01=pygrib.open('June1SFC.grib') #ERA5 June 1, 1985

GeoHeight_1000=ERA5_06_01.select(name='Geopotential', level=1000, validityTime=600)[0]
GeoHeight_1000_data=GeoHeight_1000['values']
GeoHeight_1000_dm=GeoHeight_1000_data/10

#1000 Winds (U), 
uwind1000=ERA5_06_01.select(name='U component of wind', level=1000, validityTime=600)[0]
uwind1000_data=uwind1000['values']
uwind1000_kt=uwind1000_data*1.94

#1000 Winds (V)
vwind1000=ERA5_06_01.select(name='V component of wind', level=1000, validityTime=600)[0] 
vwind1000_data=vwind1000['values']
vwind1000_kt=vwind1000_data*1.94


#1000 Temperature
temp1000=ERA5_06_01.select(name='Temperature', level=1000, validityTime=600)[0] 
temp1000_data=temp1000['values']
temp1000_F=(temp1000_data-273.15)*(9/5)+32

lats,lons=GeoHeight_1000.latlons() 


fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-100.,-70.,35.,50.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='black')
ax.add_feature(cfeature.BORDERS, edgecolor='black')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,temp1000_F,levels=bounds,cmap=plt.cm.nipy_spectral, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('Fahrenheit')



#windbarbs
ax.barbs(lons[::5,::5],lats[::5,::5],uwind1000_kt[::5,::5],vwind1000_kt[::5,::5],color='black',transform=ccrs.PlateCarree())

#1000 geoheight
ax.contour(lons,lats,GeoHeight_1000_dm,np.arange(np.min(GeoHeight_1000_dm),np.max(GeoHeight_1000_dm),15),linewidths=1.5,colors="black",transform=ccrs.PlateCarree())

plt.title('June 1, 1985 06z 1000 mb Heights (dm) / Temperature (F)')

plt.savefig('1000mb_June1_06z.png')
plt.show()
#%% 1000 hpa 18z
ERA5_06_01=pygrib.open('June1SFC.grib') #ERA5 June 1, 1985

GeoHeight_1000=ERA5_06_01.select(name='Geopotential', level=1000, validityTime=1800)[0]
GeoHeight_1000_data=GeoHeight_1000['values']
GeoHeight_1000_dm=GeoHeight_1000_data/10

#1000 Winds (U), 
uwind1000=ERA5_06_01.select(name='U component of wind', level=1000, validityTime=1800)[0]
uwind1000_data=uwind1000['values']
uwind1000_kt=uwind1000_data*1.94

#1000 Winds (V)
vwind1000=ERA5_06_01.select(name='V component of wind', level=1000, validityTime=1800)[0] 
vwind1000_data=vwind1000['values']
vwind1000_kt=vwind1000_data*1.94


#1000 Temperature
temp1000=ERA5_06_01.select(name='Temperature', level=1000, validityTime=1800)[0] 
temp1000_data=temp1000['values']
temp1000_F=(temp1000_data-273.15)*(9/5)+32

lats,lons=GeoHeight_1000.latlons() 


fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-100.,-70.,35.,50.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='black')
ax.add_feature(cfeature.BORDERS, edgecolor='black')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,temp1000_F,levels=bounds,cmap=plt.cm.nipy_spectral, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('Fahrenheit')



#windbarbs
ax.barbs(lons[::5,::5],lats[::5,::5],uwind1000_kt[::5,::5],vwind1000_kt[::5,::5],color='black',transform=ccrs.PlateCarree())

#1000 geoheight
ax.contour(lons,lats,GeoHeight_1000_dm,np.arange(np.min(GeoHeight_1000_dm),np.max(GeoHeight_1000_dm),15),linewidths=1.5,colors="black",transform=ccrs.PlateCarree())

plt.title('June 1, 1985 18z 1000 mb Heights (dm) / Temperature (F)')

plt.savefig('1000mb_June1_18z.png')
plt.show()
#%% GIF May 31-June 1
from PIL import Image

i1 = Image.open('1000mb_May31_00z.png')
i2 = Image.open('1000mb_May31_06z.png')
i3 = Image.open('1000mb_May31_12z.png')
i4 = Image.open('1000mb_May31_18z.png')
i5 = Image.open('1000mb_June1_00z.png')
i6 = Image.open('1000mb_June1_06z.png')
i7 = Image.open('1000mb_June1_18z.png')
i1.save('SFC_May31_June1.gif',
        save_all=True,
        append_images=[i2, i3, i4, i5, i6, i7],
        duration=1400,
        loop=0)