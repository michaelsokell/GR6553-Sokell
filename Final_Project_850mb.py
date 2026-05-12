import matplotlib.pyplot as plt
import numpy as np
import pygrib
import cartopy 
import cartopy.feature as cfeature
import cartopy.crs as ccrs 

#MAY 30, 1985
#%% 850 hpa 00z
ERA5_05_30=pygrib.open('19850530') #ERA5 May 30, 1985

GeoHeight_850=ERA5_05_30.select(name='Geopotential', level=850, validityTime=0)[0]
GeoHeight_850_data=GeoHeight_850['values']
GeoHeight_850_dm=GeoHeight_850_data/10

#850 Winds (U), 
uwind850=ERA5_05_30.select(name='U component of wind', level=850, validityTime=0)[0]
uwind850_data=uwind850['values']
uwind850_kt=uwind850_data*1.94

#850 Winds (V)
vwind850=ERA5_05_30.select(name='V component of wind', level=850, validityTime=0)[0] 
vwind850_data=vwind850['values']
vwind850_kt=vwind850_data*1.94

#Wmag
wmag850=np.sqrt(uwind850_data**2 + vwind850_data**2)*1.94

lats,lons=GeoHeight_850.latlons() 



fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120.,-75.,21.,55.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[15,20,25,30,35,40,45,50]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag850,levels=bounds,cmap=plt.cm.jet, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind850_kt[::30,::30],vwind850_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#850 geoheight
ax.contour(lons,lats,GeoHeight_850_dm,np.arange(np.min(GeoHeight_850_dm),np.max(GeoHeight_850_dm),30),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 30, 1985 00z 850 mb Heights (dm) / Isotachs (knots)')

plt.savefig('850mb_May30_00z.png')
plt.show()
#%% 850 hpa 06z
ERA5_05_30=pygrib.open('19850530') #ERA5 May 30, 1985

GeoHeight_850=ERA5_05_30.select(name='Geopotential', level=850, validityTime=600)[0]
GeoHeight_850_data=GeoHeight_850['values']
GeoHeight_850_dm=GeoHeight_850_data/10

#850 Winds (U), 
uwind850=ERA5_05_30.select(name='U component of wind', level=850, validityTime=600)[0]
uwind850_data=uwind850['values']
uwind850_kt=uwind850_data*1.94

#850 Winds (V)
vwind850=ERA5_05_30.select(name='V component of wind', level=850, validityTime=600)[0] 
vwind850_data=vwind850['values']
vwind850_kt=vwind850_data*1.94

#Wmag
wmag850=np.sqrt(uwind850_data**2 + vwind850_data**2)*1.94

lats,lons=GeoHeight_850.latlons() 



fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120.,-75.,21.,55.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[15,20,25,30,35,40,45,50]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag850,levels=bounds,cmap=plt.cm.jet, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind850_kt[::30,::30],vwind850_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#850 geoheight
ax.contour(lons,lats,GeoHeight_850_dm,np.arange(np.min(GeoHeight_850_dm),np.max(GeoHeight_850_dm),30),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 30, 1985 06z 850 mb Heights (dm) / Isotachs (knots)')

plt.savefig('850mb_May30_06z.png')
plt.show()
#%% 850 hpa 12z
ERA5_05_30=pygrib.open('19850530') #ERA5 May 30, 1985

GeoHeight_850=ERA5_05_30.select(name='Geopotential', level=850, validityTime=1200)[0]
GeoHeight_850_data=GeoHeight_850['values']
GeoHeight_850_dm=GeoHeight_850_data/10

#850 Winds (U), 
uwind850=ERA5_05_30.select(name='U component of wind', level=850, validityTime=1200)[0]
uwind850_data=uwind850['values']
uwind850_kt=uwind850_data*1.94

#850 Winds (V)
vwind850=ERA5_05_30.select(name='V component of wind', level=850, validityTime=1200)[0] 
vwind850_data=vwind850['values']
vwind850_kt=vwind850_data*1.94

#Wmag
wmag850=np.sqrt(uwind850_data**2 + vwind850_data**2)*1.94

lats,lons=GeoHeight_850.latlons() 



fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120.,-75.,21.,55.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[15,20,25,30,35,40,45,50]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag850,levels=bounds,cmap=plt.cm.jet, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind850_kt[::30,::30],vwind850_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#850 geoheight
ax.contour(lons,lats,GeoHeight_850_dm,np.arange(np.min(GeoHeight_850_dm),np.max(GeoHeight_850_dm),30),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 30, 1985 12z 850 mb Heights (dm) / Isotachs (knots)')

plt.savefig('850mb_May30_12z.png')
plt.show()
#%% 850 hpa 18z
ERA5_05_30=pygrib.open('19850530') #ERA5 May 30, 1985

GeoHeight_850=ERA5_05_30.select(name='Geopotential', level=850, validityTime=1800)[0]
GeoHeight_850_data=GeoHeight_850['values']
GeoHeight_850_dm=GeoHeight_850_data/10

#850 Winds (U), 
uwind850=ERA5_05_30.select(name='U component of wind', level=850, validityTime=1800)[0]
uwind850_data=uwind850['values']
uwind850_kt=uwind850_data*1.94

#850 Winds (V)
vwind850=ERA5_05_30.select(name='V component of wind', level=850, validityTime=1800)[0] 
vwind850_data=vwind850['values']
vwind850_kt=vwind850_data*1.94

#Wmag
wmag850=np.sqrt(uwind850_data**2 + vwind850_data**2)*1.94

lats,lons=GeoHeight_850.latlons() 



fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120.,-75.,21.,55.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[15,20,25,30,35,40,45,50]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag850,levels=bounds,cmap=plt.cm.jet, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind850_kt[::30,::30],vwind850_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#850 geoheight
ax.contour(lons,lats,GeoHeight_850_dm,np.arange(np.min(GeoHeight_850_dm),np.max(GeoHeight_850_dm),30),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 30, 1985 18z 850 mb Heights (dm) / Isotachs (knots)')

plt.savefig('850mb_May30_18z.png')
plt.show()
#%% MAY 31, 1985
#%% 850 hpa 00z
ERA5_05_31=pygrib.open('19850531') #ERA5 May 30, 1985

GeoHeight_850=ERA5_05_31.select(name='Geopotential', level=850, validityTime=0)[0]
GeoHeight_850_data=GeoHeight_850['values']
GeoHeight_850_dm=GeoHeight_850_data/10

#850 Winds (U), 
uwind850=ERA5_05_31.select(name='U component of wind', level=850, validityTime=0)[0]
uwind850_data=uwind850['values']
uwind850_kt=uwind850_data*1.94

#850 Winds (V)
vwind850=ERA5_05_31.select(name='V component of wind', level=850, validityTime=0)[0] 
vwind850_data=vwind850['values']
vwind850_kt=vwind850_data*1.94

#Wmag
wmag850=np.sqrt(uwind850_data**2 + vwind850_data**2)*1.94

lats,lons=GeoHeight_850.latlons() 



fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120.,-75.,21.,55.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[15,20,25,30,35,40,45,50]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag850,levels=bounds,cmap=plt.cm.jet, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind850_kt[::30,::30],vwind850_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#850 geoheight
ax.contour(lons,lats,GeoHeight_850_dm,np.arange(np.min(GeoHeight_850_dm),np.max(GeoHeight_850_dm),30),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 31, 1985 00z 850 mb Heights (dm) / Isotachs (knots)')

plt.savefig('850mb_May31_00z.png')
plt.show()
#%% 850 hpa 06z
ERA5_05_31=pygrib.open('19850531') #ERA5 May 30, 1985

GeoHeight_850=ERA5_05_31.select(name='Geopotential', level=850, validityTime=600)[0]
GeoHeight_850_data=GeoHeight_850['values']
GeoHeight_850_dm=GeoHeight_850_data/10

#850 Winds (U), 
uwind850=ERA5_05_31.select(name='U component of wind', level=850, validityTime=600)[0]
uwind850_data=uwind850['values']
uwind850_kt=uwind850_data*1.94

#850 Winds (V)
vwind850=ERA5_05_31.select(name='V component of wind', level=850, validityTime=600)[0] 
vwind850_data=vwind850['values']
vwind850_kt=vwind850_data*1.94

#Wmag
wmag850=np.sqrt(uwind850_data**2 + vwind850_data**2)*1.94

lats,lons=GeoHeight_850.latlons() 



fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120.,-75.,21.,55.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[15,20,25,30,35,40,45,50]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag850,levels=bounds,cmap=plt.cm.jet, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind850_kt[::30,::30],vwind850_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#850 geoheight
ax.contour(lons,lats,GeoHeight_850_dm,np.arange(np.min(GeoHeight_850_dm),np.max(GeoHeight_850_dm),30),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 31, 1985 06z 850 mb Heights (dm) / Isotachs (knots)')

plt.savefig('850mb_May31_06z.png')
plt.show()
#%% 850 hpa 12z
ERA5_05_31=pygrib.open('19850531') #ERA5 May 30, 1985

GeoHeight_850=ERA5_05_31.select(name='Geopotential', level=850, validityTime=1200)[0]
GeoHeight_850_data=GeoHeight_850['values']
GeoHeight_850_dm=GeoHeight_850_data/10

#850 Winds (U), 
uwind850=ERA5_05_31.select(name='U component of wind', level=850, validityTime=1200)[0]
uwind850_data=uwind850['values']
uwind850_kt=uwind850_data*1.94

#850 Winds (V)
vwind850=ERA5_05_31.select(name='V component of wind', level=850, validityTime=1200)[0] 
vwind850_data=vwind850['values']
vwind850_kt=vwind850_data*1.94

#Wmag
wmag850=np.sqrt(uwind850_data**2 + vwind850_data**2)*1.94

lats,lons=GeoHeight_850.latlons() 



fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120.,-75.,21.,55.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[15,20,25,30,35,40,45,50]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag850,levels=bounds,cmap=plt.cm.jet, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind850_kt[::30,::30],vwind850_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#850 geoheight
ax.contour(lons,lats,GeoHeight_850_dm,np.arange(np.min(GeoHeight_850_dm),np.max(GeoHeight_850_dm),30),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 31, 1985 12z 850 mb Heights (dm) / Isotachs (knots)')

plt.savefig('850mb_May31_12z.png')
plt.show()
#%% 850 hpa 18z
ERA5_05_31=pygrib.open('19850531') #ERA5 May 30, 1985

GeoHeight_850=ERA5_05_31.select(name='Geopotential', level=850, validityTime=1800)[0]
GeoHeight_850_data=GeoHeight_850['values']
GeoHeight_850_dm=GeoHeight_850_data/10

#850 Winds (U), 
uwind850=ERA5_05_31.select(name='U component of wind', level=850, validityTime=1800)[0]
uwind850_data=uwind850['values']
uwind850_kt=uwind850_data*1.94

#850 Winds (V)
vwind850=ERA5_05_31.select(name='V component of wind', level=850, validityTime=1800)[0] 
vwind850_data=vwind850['values']
vwind850_kt=vwind850_data*1.94

#Wmag
wmag850=np.sqrt(uwind850_data**2 + vwind850_data**2)*1.94

lats,lons=GeoHeight_850.latlons() 



fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120.,-75.,21.,55.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[15,20,25,30,35,40,45,50]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag850,levels=bounds,cmap=plt.cm.jet, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind850_kt[::30,::30],vwind850_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#850 geoheight
ax.contour(lons,lats,GeoHeight_850_dm,np.arange(np.min(GeoHeight_850_dm),np.max(GeoHeight_850_dm),30),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 31, 1985 18z 850 mb Heights (dm) / Isotachs (knots)')

plt.savefig('850mb_May31_18z.png')
plt.show()
#%% JUNE 1, 1985
#%% 850 hpa 00z
ERA5_06_01=pygrib.open('19850601') #ERA5 May 30, 1985

GeoHeight_850=ERA5_06_01.select(name='Geopotential', level=850, validityTime=0)[0]
GeoHeight_850_data=GeoHeight_850['values']
GeoHeight_850_dm=GeoHeight_850_data/10

#850 Winds (U), 
uwind850=ERA5_06_01.select(name='U component of wind', level=850, validityTime=0)[0]
uwind850_data=uwind850['values']
uwind850_kt=uwind850_data*1.94

#850 Winds (V)
vwind850=ERA5_06_01.select(name='V component of wind', level=850, validityTime=0)[0] 
vwind850_data=vwind850['values']
vwind850_kt=vwind850_data*1.94

#Wmag
wmag850=np.sqrt(uwind850_data**2 + vwind850_data**2)*1.94

lats,lons=GeoHeight_850.latlons() 



fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120.,-75.,21.,55.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[15,20,25,30,35,40,45,50]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag850,levels=bounds,cmap=plt.cm.jet, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind850_kt[::30,::30],vwind850_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#850 geoheight
ax.contour(lons,lats,GeoHeight_850_dm,np.arange(np.min(GeoHeight_850_dm),np.max(GeoHeight_850_dm),30),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('June 1, 1985 00z 850 mb Heights (dm) / Isotachs (knots)')

plt.savefig('850mb_June1_00z.png')
plt.show()
#%% 850 hpa 06z
ERA5_06_01=pygrib.open('19850601') #ERA5 May 30, 1985

GeoHeight_850=ERA5_06_01.select(name='Geopotential', level=850, validityTime=600)[0]
GeoHeight_850_data=GeoHeight_850['values']
GeoHeight_850_dm=GeoHeight_850_data/10

#850 Winds (U), 
uwind850=ERA5_06_01.select(name='U component of wind', level=850, validityTime=600)[0]
uwind850_data=uwind850['values']
uwind850_kt=uwind850_data*1.94

#850 Winds (V)
vwind850=ERA5_06_01.select(name='V component of wind', level=850, validityTime=600)[0] 
vwind850_data=vwind850['values']
vwind850_kt=vwind850_data*1.94

#Wmag
wmag850=np.sqrt(uwind850_data**2 + vwind850_data**2)*1.94

lats,lons=GeoHeight_850.latlons() 



fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120.,-75.,21.,55.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[15,20,25,30,35,40,45,50]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag850,levels=bounds,cmap=plt.cm.jet, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind850_kt[::30,::30],vwind850_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#850 geoheight
ax.contour(lons,lats,GeoHeight_850_dm,np.arange(np.min(GeoHeight_850_dm),np.max(GeoHeight_850_dm),30),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('June 1, 1985 06z 850 mb Heights (dm) / Isotachs (knots)')

plt.savefig('850mb_June1_06z.png')
plt.show()
#%% 850 hpa 18z
ERA5_06_01=pygrib.open('19850601') #ERA5 May 30, 1985

GeoHeight_850=ERA5_06_01.select(name='Geopotential', level=850, validityTime=1800)[0]
GeoHeight_850_data=GeoHeight_850['values']
GeoHeight_850_dm=GeoHeight_850_data/10

#850 Winds (U), 
uwind850=ERA5_06_01.select(name='U component of wind', level=850, validityTime=1800)[0]
uwind850_data=uwind850['values']
uwind850_kt=uwind850_data*1.94

#850 Winds (V)
vwind850=ERA5_06_01.select(name='V component of wind', level=850, validityTime=1800)[0] 
vwind850_data=vwind850['values']
vwind850_kt=vwind850_data*1.94

#Wmag
wmag850=np.sqrt(uwind850_data**2 + vwind850_data**2)*1.94

lats,lons=GeoHeight_850.latlons() 



fg=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-120.,-75.,21.,55.])
ax.add_feature(cfeature.LAND, color='wheat')
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.COASTLINE, edgecolor='grey')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.add_feature(cfeature.LAKES, color='lightblue') 
gl=ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,color='lightgray',alpha=1,linewidth=2,linestyle='--')
gl.left_labels=False 
gl.right_labels=True


bounds=[15,20,25,30,35,40,45,50]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag850,levels=bounds,cmap=plt.cm.jet, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind850_kt[::30,::30],vwind850_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#850 geoheight
ax.contour(lons,lats,GeoHeight_850_dm,np.arange(np.min(GeoHeight_850_dm),np.max(GeoHeight_850_dm),30),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('June 1, 1985 18z 850 mb Heights (dm) / Isotachs (knots)')

plt.savefig('850mb_June1_18z.png')
plt.show()

#%% GIF May 30
from PIL import Image

i1 = Image.open('850mb_May30_00z.png')
i2 = Image.open('850mb_May30_06z.png')
i3 = Image.open('850mb_May30_12z.png')
i4 = Image.open('850mb_May30_18z.png')
i1.save('850mb_May30.gif',
        save_all=True,
        append_images=[i2, i3, i4],
        duration=1400,
        loop=0)
#%% GIF May 31
from PIL import Image

i1 = Image.open('850mb_May31_00z.png')
i2 = Image.open('850mb_May31_06z.png')
i3 = Image.open('850mb_May31_12z.png')
i4 = Image.open('850mb_May31_18z.png')
i1.save('850mb_May31.gif',
        save_all=True,
        append_images=[i2, i3, i4],
        duration=1400,
        loop=0)
#%% GIF June 1
from PIL import Image

i1 = Image.open('850mb_June1_00z.png')
i2 = Image.open('850mb_June1_06z.png')
i3 = Image.open('850mb_June1_18z.png')
i1.save('850mb_June1.gif',
        save_all=True,
        append_images=[i2, i3],
        duration=1400,
        loop=0)