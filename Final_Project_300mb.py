import matplotlib.pyplot as plt
import numpy as np
import pygrib
import cartopy 
import cartopy.feature as cfeature
import cartopy.crs as ccrs 

#MAY 30, 1985
#%% 300 hpa 0z
ERA5_05_30=pygrib.open('19850530') #ERA5 May 30, 1985

GeoHeight_300=ERA5_05_30.select(name='Geopotential', level=300, validityTime=0)[0]
GeoHeight_300_data=GeoHeight_300['values']
GeoHeight_300_dm=GeoHeight_300_data/10

#300 Winds (U), 
uwind300=ERA5_05_30.select(name='U component of wind', level=300, validityTime=0)[0]
uwind300_data=uwind300['values']
uwind300_kt=uwind300_data*1.94

#300 Winds (V)
vwind300=ERA5_05_30.select(name='V component of wind', level=300, validityTime=0)[0] 
vwind300_data=vwind300['values']
vwind300_kt=vwind300_data*1.94

#Wmag
wmag300=np.sqrt(uwind300_data**2 + vwind300_data**2)*1.94

lats,lons=GeoHeight_300.latlons() 



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


bounds=[30,40,50,60,80,100,125,150,200]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag300,levels=bounds,cmap=plt.cm.YlOrRd, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind300_kt[::30,::30],vwind300_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#300 geoheight
ax.contour(lons,lats,GeoHeight_300_dm,np.arange(np.min(GeoHeight_300_dm),np.max(GeoHeight_300_dm),60),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 30, 1985 00z 300 mb Heights (dm) / Isotachs (knots)')

plt.savefig('300mb_May30_00z.png')
plt.show()
#%% 300 hpa 06z
ERA5_05_30=pygrib.open('19850530') #ERA5 May 30, 1985

GeoHeight_300=ERA5_05_30.select(name='Geopotential', level=300, validityTime=600)[0]
GeoHeight_300_data=GeoHeight_300['values']
GeoHeight_300_dm=GeoHeight_300_data/10

#300 Winds (U), 
uwind300=ERA5_05_30.select(name='U component of wind', level=300, validityTime=600)[0]
uwind300_data=uwind300['values']
uwind300_kt=uwind300_data*1.94

#300 Winds (V)
vwind300=ERA5_05_30.select(name='V component of wind', level=300, validityTime=600)[0] 
vwind300_data=vwind300['values']
vwind300_kt=vwind300_data*1.94

#Wmag
wmag300=np.sqrt(uwind300_data**2 + vwind300_data**2)*1.94

lats,lons=GeoHeight_300.latlons() 



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


bounds=[30,40,50,60,80,100,125,150,200]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag300,levels=bounds,cmap=plt.cm.YlOrRd, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind300_kt[::30,::30],vwind300_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#300 geoheight
ax.contour(lons,lats,GeoHeight_300_dm,np.arange(np.min(GeoHeight_300_dm),np.max(GeoHeight_300_dm),60),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 30, 1985 06z 300 mb Heights (dm) / Isotachs (knots)')

plt.savefig('300mb_May30_06z.png')
plt.show()
#%% 300 hpa 12z
ERA5_05_30=pygrib.open('19850530') #ERA5 May 30, 1985

GeoHeight_300=ERA5_05_30.select(name='Geopotential', level=300, validityTime=1200)[0]
GeoHeight_300_data=GeoHeight_300['values']
GeoHeight_300_dm=GeoHeight_300_data/10

#300 Winds (U), 
uwind300=ERA5_05_30.select(name='U component of wind', level=300, validityTime=1200)[0]
uwind300_data=uwind300['values']
uwind300_kt=uwind300_data*1.94

#300 Winds (V)
vwind300=ERA5_05_30.select(name='V component of wind', level=300, validityTime=1200)[0] 
vwind300_data=vwind300['values']
vwind300_kt=vwind300_data*1.94

#Wmag
wmag300=np.sqrt(uwind300_data**2 + vwind300_data**2)*1.94

lats,lons=GeoHeight_300.latlons() 



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


bounds=[30,40,50,60,80,100,125,150,200]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag300,levels=bounds,cmap=plt.cm.YlOrRd, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind300_kt[::30,::30],vwind300_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#300 geoheight
ax.contour(lons,lats,GeoHeight_300_dm,np.arange(np.min(GeoHeight_300_dm),np.max(GeoHeight_300_dm),60),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 30, 1985 12z 300 mb Heights (dm) / Isotachs (knots)')

plt.savefig('300mb_May30_12z.png')
plt.show()
#%% 300 hpa 18z
ERA5_05_30=pygrib.open('19850530') #ERA5 May 30, 1985

GeoHeight_300=ERA5_05_30.select(name='Geopotential', level=300, validityTime=1800)[0]
GeoHeight_300_data=GeoHeight_300['values']
GeoHeight_300_dm=GeoHeight_300_data/10

#300 Winds (U), 
uwind300=ERA5_05_30.select(name='U component of wind', level=300, validityTime=1800)[0]
uwind300_data=uwind300['values']
uwind300_kt=uwind300_data*1.94

#300 Winds (V)
vwind300=ERA5_05_30.select(name='V component of wind', level=300, validityTime=1800)[0] 
vwind300_data=vwind300['values']
vwind300_kt=vwind300_data*1.94

#Wmag
wmag300=np.sqrt(uwind300_data**2 + vwind300_data**2)*1.94

lats,lons=GeoHeight_300.latlons() 



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


bounds=[30,40,50,60,80,100,125,150,200]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag300,levels=bounds,cmap=plt.cm.YlOrRd, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind300_kt[::30,::30],vwind300_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#300 geoheight
ax.contour(lons,lats,GeoHeight_300_dm,np.arange(np.min(GeoHeight_300_dm),np.max(GeoHeight_300_dm),60),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 30, 1985 18z 300 mb Heights (dm) / Isotachs (knots)')

plt.savefig('300mb_May30_18z.png')
plt.show()
#%% MAY 31, 1985
#%% 300 hpa 00z
ERA5_05_31=pygrib.open('19850531') #ERA5 May 31, 1985

GeoHeight_300=ERA5_05_31.select(name='Geopotential', level=300, validityTime=0)[0]
GeoHeight_300_data=GeoHeight_300['values']
GeoHeight_300_dm=GeoHeight_300_data/10

#300 Winds (U), 
uwind300=ERA5_05_31.select(name='U component of wind', level=300, validityTime=0)[0]
uwind300_data=uwind300['values']
uwind300_kt=uwind300_data*1.94

#300 Winds (V)
vwind300=ERA5_05_31.select(name='V component of wind', level=300, validityTime=0)[0] 
vwind300_data=vwind300['values']
vwind300_kt=vwind300_data*1.94

#Wmag
wmag300=np.sqrt(uwind300_data**2 + vwind300_data**2)*1.94

lats,lons=GeoHeight_300.latlons() 



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


bounds=[30,40,50,60,80,100,125,150,200]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag300,levels=bounds,cmap=plt.cm.YlOrRd, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind300_kt[::30,::30],vwind300_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#300 geoheight
ax.contour(lons,lats,GeoHeight_300_dm,np.arange(np.min(GeoHeight_300_dm),np.max(GeoHeight_300_dm),60),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 31, 1985 00z 300 mb Heights (dm) / Isotachs (knots)')

plt.savefig('300mb_May31_00z.png')
plt.show()
#%% 300 hpa 06z
ERA5_05_31=pygrib.open('19850531') #ERA5 May 31, 1985

GeoHeight_300=ERA5_05_31.select(name='Geopotential', level=300, validityTime=600)[0]
GeoHeight_300_data=GeoHeight_300['values']
GeoHeight_300_dm=GeoHeight_300_data/10

#300 Winds (U), 
uwind300=ERA5_05_31.select(name='U component of wind', level=300, validityTime=600)[0]
uwind300_data=uwind300['values']
uwind300_kt=uwind300_data*1.94

#300 Winds (V)
vwind300=ERA5_05_31.select(name='V component of wind', level=300, validityTime=600)[0] 
vwind300_data=vwind300['values']
vwind300_kt=vwind300_data*1.94

#Wmag
wmag300=np.sqrt(uwind300_data**2 + vwind300_data**2)*1.94

lats,lons=GeoHeight_300.latlons() 



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


bounds=[30,40,50,60,80,100,125,150,200]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag300,levels=bounds,cmap=plt.cm.YlOrRd, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind300_kt[::30,::30],vwind300_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#300 geoheight
ax.contour(lons,lats,GeoHeight_300_dm,np.arange(np.min(GeoHeight_300_dm),np.max(GeoHeight_300_dm),60),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 31, 1985 06z 300 mb Heights (dm) / Isotachs (knots)')

plt.savefig('300mb_May31_06z.png')
plt.show()
#%% 300 hpa 12z
ERA5_05_31=pygrib.open('19850531') #ERA5 May 31, 1985

GeoHeight_300=ERA5_05_31.select(name='Geopotential', level=300, validityTime=1200)[0]
GeoHeight_300_data=GeoHeight_300['values']
GeoHeight_300_dm=GeoHeight_300_data/10

#300 Winds (U), 
uwind300=ERA5_05_31.select(name='U component of wind', level=300, validityTime=1200)[0]
uwind300_data=uwind300['values']
uwind300_kt=uwind300_data*1.94

#300 Winds (V)
vwind300=ERA5_05_31.select(name='V component of wind', level=300, validityTime=1200)[0] 
vwind300_data=vwind300['values']
vwind300_kt=vwind300_data*1.94

#Wmag
wmag300=np.sqrt(uwind300_data**2 + vwind300_data**2)*1.94

lats,lons=GeoHeight_300.latlons() 



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


bounds=[30,40,50,60,80,100,125,150,200]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag300,levels=bounds,cmap=plt.cm.YlOrRd, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind300_kt[::30,::30],vwind300_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#300 geoheight
ax.contour(lons,lats,GeoHeight_300_dm,np.arange(np.min(GeoHeight_300_dm),np.max(GeoHeight_300_dm),60),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 31, 1985 12z 300 mb Heights (dm) / Isotachs (knots)')

plt.savefig('300mb_May31_12z.png')
plt.show()
#%% 300 hpa 18z
ERA5_05_31=pygrib.open('19850531') #ERA5 May 31, 1985

GeoHeight_300=ERA5_05_31.select(name='Geopotential', level=300, validityTime=1800)[0]
GeoHeight_300_data=GeoHeight_300['values']
GeoHeight_300_dm=GeoHeight_300_data/10

#300 Winds (U), 
uwind300=ERA5_05_31.select(name='U component of wind', level=300, validityTime=1800)[0]
uwind300_data=uwind300['values']
uwind300_kt=uwind300_data*1.94

#300 Winds (V)
vwind300=ERA5_05_31.select(name='V component of wind', level=300, validityTime=1800)[0] 
vwind300_data=vwind300['values']
vwind300_kt=vwind300_data*1.94

#Wmag
wmag300=np.sqrt(uwind300_data**2 + vwind300_data**2)*1.94

lats,lons=GeoHeight_300.latlons() 



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


bounds=[30,40,50,60,80,100,125,150,200]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag300,levels=bounds,cmap=plt.cm.YlOrRd, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind300_kt[::30,::30],vwind300_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#300 geoheight
ax.contour(lons,lats,GeoHeight_300_dm,np.arange(np.min(GeoHeight_300_dm),np.max(GeoHeight_300_dm),60),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('May 31, 1985 18z 300 mb Heights (dm) / Isotachs (knots)')

plt.savefig('300mb_May31_18z.png')
plt.show()
#%% MAY 31, 1985
#%% 300 hpa 00z
ERA5_06_01=pygrib.open('19850601') #ERA5 May 31, 1985

GeoHeight_300=ERA5_06_01.select(name='Geopotential', level=300, validityTime=0)[0]
GeoHeight_300_data=GeoHeight_300['values']
GeoHeight_300_dm=GeoHeight_300_data/10

#300 Winds (U), 
uwind300=ERA5_06_01.select(name='U component of wind', level=300, validityTime=0)[0]
uwind300_data=uwind300['values']
uwind300_kt=uwind300_data*1.94

#300 Winds (V)
vwind300=ERA5_06_01.select(name='V component of wind', level=300, validityTime=0)[0] 
vwind300_data=vwind300['values']
vwind300_kt=vwind300_data*1.94

#Wmag
wmag300=np.sqrt(uwind300_data**2 + vwind300_data**2)*1.94

lats,lons=GeoHeight_300.latlons() 



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


bounds=[30,40,50,60,80,100,125,150,200]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag300,levels=bounds,cmap=plt.cm.YlOrRd, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind300_kt[::30,::30],vwind300_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#300 geoheight
ax.contour(lons,lats,GeoHeight_300_dm,np.arange(np.min(GeoHeight_300_dm),np.max(GeoHeight_300_dm),60),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('June 1, 1985 00z 300 mb Heights (dm) / Isotachs (knots)')

plt.savefig('300mb_June1_00z.png')
plt.show()
#%% 300 hpa 06z
ERA5_06_01=pygrib.open('19850601') #ERA5 May 31, 1985

GeoHeight_300=ERA5_06_01.select(name='Geopotential', level=300, validityTime=600)[0]
GeoHeight_300_data=GeoHeight_300['values']
GeoHeight_300_dm=GeoHeight_300_data/10

#300 Winds (U), 
uwind300=ERA5_06_01.select(name='U component of wind', level=300, validityTime=600)[0]
uwind300_data=uwind300['values']
uwind300_kt=uwind300_data*1.94

#300 Winds (V)
vwind300=ERA5_06_01.select(name='V component of wind', level=300, validityTime=600)[0] 
vwind300_data=vwind300['values']
vwind300_kt=vwind300_data*1.94

#Wmag
wmag300=np.sqrt(uwind300_data**2 + vwind300_data**2)*1.94

lats,lons=GeoHeight_300.latlons() 



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


bounds=[30,40,50,60,80,100,125,150,200]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag300,levels=bounds,cmap=plt.cm.YlOrRd, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')



#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind300_kt[::30,::30],vwind300_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#300 geoheight
ax.contour(lons,lats,GeoHeight_300_dm,np.arange(np.min(GeoHeight_300_dm),np.max(GeoHeight_300_dm),60),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('June 1, 1985 06z 300 mb Heights (dm) / Isotachs (knots)')

plt.savefig('300mb_June1_06z.png')
plt.show()
#%% 300 hpa 18z
ERA5_06_01=pygrib.open('19850601') #ERA5 May 31, 1985

GeoHeight_300=ERA5_06_01.select(name='Geopotential', level=300, validityTime=1800)[0]
GeoHeight_300_data=GeoHeight_300['values']
GeoHeight_300_dm=GeoHeight_300_data/10

#300 Winds (U), 
uwind300=ERA5_06_01.select(name='U component of wind', level=300, validityTime=1800)[0]
uwind300_data=uwind300['values']
uwind300_kt=uwind300_data*1.94

#300 Winds (V)
vwind300=ERA5_06_01.select(name='V component of wind', level=300, validityTime=1800)[0] 
vwind300_data=vwind300['values']
vwind300_kt=vwind300_data*1.94

#Wmag
wmag300=np.sqrt(uwind300_data**2 + vwind300_data**2)*1.94

lats,lons=GeoHeight_300.latlons() 



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


bounds=[30,40,50,60,80,100,125,150,200]
  

#put data on figure 
#wmag contour
ca=ax.contourf(lons,lats,wmag300,levels=bounds,cmap=plt.cm.YlOrRd, transform=ccrs.PlateCarree())
cbar=plt.colorbar(ca,location='bottom')
cbar.set_label('knots')

#windbarbs
ax.barbs(lons[::30,::30],lats[::30,::30],uwind300_kt[::30,::30],vwind300_kt[::30,::30],color='black',transform=ccrs.PlateCarree())

#300 geoheight
ax.contour(lons,lats,GeoHeight_300_dm,np.arange(np.min(GeoHeight_300_dm),np.max(GeoHeight_300_dm),60),linewidths=1,colors="black",transform=ccrs.PlateCarree())

plt.title('June 1, 1985 18z 300 mb Heights (dm) / Isotachs (knots)')

plt.savefig('300mb_June1_18z.png')
plt.show()
#%% GIF May 30
from PIL import Image

i1 = Image.open('300mb_May30_00z.png')
i2 = Image.open('300mb_May30_06z.png')
i3 = Image.open('300mb_May30_12z.png')
i4 = Image.open('300mb_May30_18z.png')
i1.save('300mb_May30.gif',
        save_all=True,
        append_images=[i2, i3, i4],
        duration=1400,
        loop=0)
#%% GIF May 31
from PIL import Image

i1 = Image.open('300mb_May31_00z.png')
i2 = Image.open('300mb_May31_06z.png')
i3 = Image.open('300mb_May31_12z.png')
i4 = Image.open('300mb_May31_18z.png')
i1.save('300mb_May31.gif',
        save_all=True,
        append_images=[i2, i3, i4],
        duration=1400,
        loop=0)
#%% GIF June1
from PIL import Image

i1 = Image.open('300mb_June1_00z.png')
i2 = Image.open('300mb_June1_06z.png')
i3 = Image.open('300mb_June1_18z.png')
i1.save('300mb_June1.gif',
        save_all=True,
        append_images=[i2, i3],
        duration=1400,
        loop=0)