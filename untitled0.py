#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:55:12 2021

@author: vmalagonsantos
"""


import netCDF4 as nc
import numpy as np
import numpy.ma as ma
import matplotlib as mpl
import matplotlib.pyplot as plt
# import cartopy as ccrs
import cartopy as cart
from cartopy import crs as ccrs

from global_land_mask import globe


# Load in the data
fn = '/Users/vmalagonsantos/OneDrive - NIOZ/Documents/IPCC-data/regional/final_projections/figure_data/pb_1e/ssp119/glaciers-ipccar6-gmipemuglaciers-ssp119_localsl_figuredata.nc'

# Read data
ds = nc.Dataset(fn)

# Create varialbles
lat = ds['lat'][:]
lon = ds['lon'][:]
id = ds['id'][:]
years = ds['years'][:]
quantiles = ds['quantiles'][:]
localSL_quantiles = ds['localSL_quantiles'][:]

is_in_ocean = globe.is_ocean(lat, lon)



#%% Make some plots
let = ['(a)','(b)','(c)','(d)','(e)','(f)','(g)','(h)','(i)','(j)']
fs = 4
    
for j in range(0,1):

    # set up figure
    fig = plt.figure(dpi=600) # indicate resolution
    

    for i in range(0,9):
        ax = fig.add_subplot(3,3,i+1,projection=ccrs.PlateCarree()) # create actual axes. You can also set up projeciton here
    
        print(i)
        #   plotting 
    
        # fig1 = ax.tricontourf(lon,lat,localSL_quantiles[1,:,5])
        ax.add_feature(cart.feature.LAND, zorder=100, edgecolor='k', linewidth= 0.1)
    
        fig1 = ax.tricontourf(lon[is_in_ocean],lat[is_in_ocean],localSL_quantiles[j,is_in_ocean,i], vmin=np.min(localSL_quantiles[:,is_in_ocean,:]), vmax=np.max(localSL_quantiles[:,is_in_ocean,:]))
        ax.coastlines() # add coastlines
    
        ax.text(0, 1.05, let[i] + ' ' + str(years[i]), transform = ax.transAxes, fontsize=fs) # Remeber: correction is set for all plot in fig.add_subplot. Transform needs to be used to convert data in a differect projection
    
    
        # color bar
        cb = plt.colorbar(fig1, orientation='horizontal')
        # cb.ax.set_yticklabels(['0','1','2','>3'])
        cb.set_label('mm',fontsize=fs)
        # Adjust as appropriate.
        cb.ax.tick_params(labelsize=fs)
        # fig.colorbar(fig1, orientation='horizontal')
        # ax.set_global()
    
    fig.subplots_adjust(hspace=0.5)
    
    plt.savefig('holi.png', dpi = 600)

    
    # fig.tight_layout(pad=3.0)
    
    ##need to figure how how to applythe same colorbar scale for all subplotsL
    ##saving plots automatically
    ##






