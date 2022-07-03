import xarray as xr

'''
Group PFTs into vegetation groups:
Evergreen trees/ forest
Deciduous/summergreen/raingreen trees/forest
Shrubs
Savanna
C3 Grasses
C4 Grasses
C3 Agriculture (pasture and crop)
C4 Agriculture (pasture and crop)
Bare
Other
'''

var='landCoverFrac'

def vegetation_groups(DGVM):
    ds = xr.open_dataset('../landCoverFrac_S2_halfdegree/'+DGVM+
                         '_S2_landCoverFrac.nc', decode_times=decode_times)

    if DGVM == 'CABLE-POP':
        decode_times=True
        '''
        0=Evergreen Needleleaf Forest
        1=Evergreen Broadleaf Forest
        2=Deciduous Needleleaf Forest
        3=Deciduous Broadleaf Forest
        4=shrub
        5=C3 grass
        6=C4 grass
        7=tundra
        8=barren
        9=ice
        '''
        ds['EVG'] = ds[var].sel(PFT=0)+ds[var].sel(PFT=1)
        ds['DCD'] = ds[var].sel(PFT=2)+ds[var].sel(PFT=3)
        ds['Shrub'] = ds[var].sel(PFT=4)
        ds['C3G'] = ds[var].sel(PFT=5)
        ds['C4G'] = ds[var].sel(PFT=5)
        ds['C3Agr'] = ds[var].sel(PFT=5)
        ds['C4Agr'] = ds[var].sel(PFT=5)
        ds['Other'] = ds[var].sel(PFT=7)
        ds['Bare'] = ds[var].sel(PFT=8)+ds[var].sel(PFT=9)

    elif DGVM == 'CLASS-CTEM':
        decode_times=True
        '''
        1-needleleaf evergreen
        2-needleleaf deciduous
        3-broadleaf evergreen
        4-broadleaf cold deciduous
        5- broadleaf drought/dry deciduous
        6-C3 crop
        7-C4 crop
        8-C3 grass
        9-C4 grass
        10-bareground
        '''
        ds['EVG'] = ds[var].sel(PFT=1)+ds[var].sel(PFT=3)
        ds['DCD'] = ds[var].sel(PFT=2)+ds[var].sel(PFT=4)+ds[var].sel(PFT=5)
        ds['Shrub'] = ds[var].sel(PFT=4)
        ds['C3G'] = ds[var].sel(PFT=8)
        ds['C4G'] = ds[var].sel(PFT=9)
        ds['C3Agr'] = ds[var].sel(PFT=6)
        ds['C4Agr'] = ds[var].sel(PFT=7)
        ds['Other'] = xr.zeros_like(ds['EVG'])
        ds['Bare'] = xr.zeros_like(ds['EVG'])

    elif DGVM == 'CLM5.0':
        decode_times=True
        '''
        Counting from 0 instead of 1
        "Level 1: not vegetated \n",
        "Level 2: needleleaf_evergreen_temperate_tree \n",
        "Level 3: needleleaf_evergreen_boreal_tree\t\n",
        "Level 4: needleleaf_deciduous_boreal_tree\t\n",
        "Level 5: broadleaf_evergreen_tropical_tree \n",
        "Level 6: broadleaf_evergreen_temperate_tree \n",
        "Level 7: broadleaf_deciduous_tropical_tree \n",
        "Level 8: broadleaf_deciduous_temperate_tree\t\n",
        "Level 9: broadleaf_deciduous_boreal_tree \n",
        "Level 10: broadleaf_evergreen_shrub \n",
        "Level 11: broadleaf_deciduous_temperate_shrub \n",
        "Level 12: broadleaf_deciduous_boreal_shrub \n",
        "Level 13: c3_arctic_grass \n",
        "Level 14: c3_non-arctic_grass \n",
        "Level 15: c4_grass \n",
        "Level 16: c3_crop \n",
        "Level 17: c3_irrigated \n",
        "Level 18: temperate_corn \n", C4
        "Level 19: irrigated_temperate_corn \n", C4
        "Level 20: spring_wheat \n",
        "Level 21: irrigated_spring_wheat \n",
        "Level 22: temperate_soybean \n",
        "Level 23: irrigated_temperate_soybean \n",
        "Level 24: cotton \n",
        "Level 25: irrigated_cotton \n",
        "Level 26: rice \n",
        "Level 27: irrigated_rice \n",
        "Level 28: sugarcane \n", C4
        "Level 29: irrigated_sugarcane \n", C4
        "Level 30: tropical_corn \n", C4
        "Level 31: irrigated_tropical_corn \n", C4
        "Level 32: tropical_soybean \n",
        "Level 33: irrigated_tropical_soybean" ;
        '''
        ds['EVG'] = ds[var].sel(PFT=1)+ds[var].sel(PFT=2)+ds[var].sel(PFT=4)+\
                    ds[var].sel(PFT=5)
        ds['DCD'] = ds[var].sel(PFT=3)+ds[var].sel(PFT=6)+ds[var].sel(PFT=7)
        ds['Shrub'] = ds[var].sel(PFT=9)+ds[var].sel(PFT=10)+ds[var].sel(PFT=11)
        ds['C3G'] = ds[var].sel(PFT=12)+ds[var].sel(PFT=13)
        ds['C4G'] = ds[var].sel(PFT=14)
        ds['C3Agr'] = ds[var].sel(PFT=15)+ds[var].sel(PFT=16)++ds[var].sel(PFT=19)+\
                      ds[var].sel(PFT=20)+ds[var].sel(PFT=21)+ds[var].sel(PFT=22)+\
                      ds[var].sel(PFT=23)+ds[var].sel(PFT=24)+ds[var].sel(PFT=25)+\
                      ds[var].sel(PFT=26)+ds[var].sel(PFT=31)+ds[var].sel(PFT=32)
        ds['C4Agr'] = ds[var].sel(PFT=17)+ds[var].sel(PFT=18)+ds[var].sel(PFT=27)+\
                      ds[var].sel(PFT=28)+ds[var].sel(PFT=29)+ds[var].sel(PFT=30)
        ds['Other'] = xr.zeros_like(ds['EVG'])
        ds['Bare'] = ds[var].sel(PFT=0)

    elif DGVM == 'ISAM':
        decode_times=False
        '''
        Counting from 0 instead of 1
        1.  Tropical evergreen
        2.  Tropical deciduous
        3.  Temperate evergreen
        4.  Temperate deciduous
        5.  Boreal evergreen forest
        6.  Savanna
        7.  C3 Grassland
        8.  Shrubland
        9.  Tundra
        10. Desert
        11. Polar desert
        12. C3 Crop
        13. C3 Pastureland
        14-18. Secondary forest of 1-5
        19. Bare ground
        20. Boreal deciduous forest
        21. C4 grassland
        22. C4 crop
        23. C4 pastureland
        24. Secondary boreal deciduous forest
        '''
        ds['EVG'] = ds[var].sel(PFT=0)+ds[var].sel(PFT=2)+ds[var].sel(PFT=4)+\
                    ds[var].sel(PFT=14)+ds[var].sel(PFT=15)+ds[var].sel(PFT=17)
        ds['DCD'] = ds[var].sel(PFT=1)+ds[var].sel(PFT=3)+ds[var].sel(PFT=19)+\
                    ds[var].sel(PFT=23)+ds[var].sel(PFT=14)+ds[var].sel(PFT=16)
        ds['Shrub'] = ds[var].sel(PFT=7)
        ds['C3G'] = ds[var].sel(PFT=6)
        ds['C4G'] = ds[var].sel(PFT=20)
        ds['C3Agr'] = ds[var].sel(PFT=11)+ds[var].sel(PFT=12)
        ds['C4Agr'] = ds[var].sel(PFT=21)+ds[var].sel(PFT=22)
        ds['Other'] = ds[var].sel(PFT=5)+ds[var].sel(PFT=8)+ds[var].sel(PFT=9)+\
                      ds[var].sel(PFT=10)
        ds['Bare'] = ds[var].sel(PFT=18)

    elif DGVM == 'ISBA-CTRIP':
        decode_times=False
        '''
        1 "Bare_soil",
        2 "Rock",
        3 "Permanent_snow",
        4 "Temperate_broad-leaved_decidus",
        5 "Boreal_needleaf_evergreen",
        6 "Tropical_broad-leaved_evergreen",
        7 "C3_crop",
        8 "C4_crop",
        9 "Irrigated_crop", ### C3 crops!
        10 "C3_grass",
        11"C4_grass",
        12 "Wetland",
        13 "Tropical_broad-leaved_decidus",
        14 "Temperate_broad-leaved_evergreen",
        15 "Temperate_needleaf_evergreen",
        16 "Boreal_broad-leaved_decidus",
        17 "Boreal_needleaf_decidus",
        18 "Tundra_grass",
        19 "Shrub" ;
        '''
        ds['EVG'] = ds[var].sel(PFT=5)+ds[var].sel(PFT=6)+ds[var].sel(PFT=14)+\
                    ds[var].sel(PFT=15)
        ds['DCD'] = ds[var].sel(PFT=4)+ds[var].sel(PFT=13)+ds[var].sel(PFT=16)+\
                    ds[var].sel(PFT=17)
        ds['Shrub'] = ds[var].sel(PFT=19)
        ds['C3G'] = ds[var].sel(PFT=10)+ds[var].sel(PFT=18)
        ds['C4G'] = ds[var].sel(PFT=11)
        ds['C3Agr'] = ds[var].sel(PFT=7)+ds[var].sel(PFT=9)
        ds['C4Agr'] = ds[var].sel(PFT=8)
        ds['Other'] = ds[var].sel(PFT=2)+ds[var].sel(PFT=3)+ds[var].sel(PFT=12)
        ds['Bare'] = ds[var].sel(PFT=1)

    elif DGVM == 'JSBACH':
        decode_times=True
        '''
        "PFT1:  Bare land",
        "PFT2:  Glacier",
        "PFT3:  Tropical evergreen trees",
        "PFT4:  Tropical deciduous trees",
        "PFT5:  Extra-tropical evergreen trees",
        "PFT6:  Extra-tropical deciduous trees",
        "PFT7:  Raingreen shrubs",
        "PFT8:  Deciduous shrubs",
        "PFT9:  C3 grass",
        "PFT10: C4 grass",
        "PFT11: C3 pasture",
        "PFT12: C4 pasture",
        "PFT13: C3 Crops",
        "PFT14: C4 Crops" ;
        '''
        ds['EVG'] = ds[var].sel(PFT=3)+ds[var].sel(PFT=5)
        ds['DCD'] = ds[var].sel(PFT=4)+ds[var].sel(PFT=6)
        ds['Shrub'] = ds[var].sel(PFT=7)+ds[var].sel(PFT=8)
        ds['C3G'] = ds[var].sel(PFT=9)
        ds['C4G'] = ds[var].sel(PFT=10)
        ds['C3Agr'] = ds[var].sel(PFT=11)+ds[var].sel(PFT=13)
        ds['C4Agr'] = ds[var].sel(PFT=12)+ds[var].sel(PFT=14)
        ds['Other'] = ds[var].sel(PFT=2)
        ds['Bare'] = ds[var].sel(PFT=1)

    elif DGVM == 'JULES-ES':
        decode_times=True
        '''
        0.BdlDcd
        1.BdlEvgTrop
        2.BdlEvgTemp
        3.NdlDcd
        4.NdlEvg
        5.c3grass
        6.c3crop
        7.c3pasture
        8.c4grass
        9.c4crop
        10.c4pasture
        11.shrubDcd
        12.shrubEvg
        13.urban
        14.lake
        15.soil
        16.ice
        '''
        ds['EVG'] = ds[var].sel(vegtype=1)+ds[var].sel(vegtype=2)
        ds['DCD'] = ds[var].sel(vegtype=0)+ds[var].sel(vegtype=3)
        ds['Shrub'] = ds[var].sel(vegtype=10)+ds[var].sel(vegtype=11)
        ds['C3G'] = ds[var].sel(vegtype=4)
        ds['C4G'] = ds[var].sel(vegtype=7)
        ds['C3Agr'] = ds[var].sel(vegtype=5)+ds[var].sel(vegtype=6)
        ds['C4Agr'] = ds[var].sel(vegtype=8)+ds[var].sel(vegtype=9)
        ds['Other'] = ds[var].sel(vegtype=12)+ds[var].sel(vegtype=13)+\
                      ds[var].sel(vegtype=14)+ds[var].sel(vegtype=15)
        ds['Bare'] = xr.zeros_like(ds['EVG'])

    elif DGVM == 'LPJ-GUESS':
        decode_times=True
        '''
        1:Boreal needleleaf evergreen (BNE)
        2:Boreal shade-intolerant needleleaf evergreen (BINE)
        3:Boreal needleleaf summergreen (BNS)
        4:Temperate needleleaf evergreen (TeNE)
        5:Temperate broadleaf summergreen (TeBS)
        6:Temperate shade-intolerant broadleaf summergreen (IBS)
        7:Temperate broadleaf evergreen (TeBE)
        8:Tropical broadleaf evergreen (TrBE)
        9:Tropical shade-intolerant broadleaf evergreen (TrIBE)
        10:Tropical broadleaf raingreen (TrBR)
        11:C3 grass (C3G)
        12:C4 grass (C4G)
        13:C3 grass in pasture (C3G_pas)
        14:C4 grass in pasture (C4G_pas)
        15:C3 annual crops (wheat w/o ccg) (CC3ann)
        16:C3 perennial crops (summer wheat w/ ccg) (CC3per)
        17:C3 nitrogen-fixing crops (summer wheat w/o ccg) (CC3nfx)
        18:C4 annual crops (corn w/o ccg) (CC4ann)
        19:C4 perennial crops (corn w/ ccg) (CC4per)
        20:C3 annual crops irrigated (wheat w/o ccg) (CC3anni)
        21:C3 perennial crops irrigated (summer wheat w/ ccg) (CC3peri)
        22:C3 nitrogen-fixing crops irrigated (summer wheat w/o ccg) (CC3nfxi)
        23:C4 annual crops irrigated (corn w/o ccg) (CC4anni)
        24:C4 perennial crops irrigated (corn w/ ccg) (CC4peri)
        25:C3 cover crop grass (ccg) (CC3G_ic)
        26:C4 cover crop grass (ccg) (CC4G_ic)
        '''
        ds['EVG'] = ds[var].sel(PFT=1)+ds[var].sel(PFT=2)+ds[var].sel(PFT=4)+\
                    ds[var].sel(PFT=7)+ds[var].sel(PFT=8)+ds[var].sel(PFT=9)
        ds['DCD'] = ds[var].sel(PFT=3)+ds[var].sel(PFT=5)+ds[var].sel(PFT=6)+\
                    ds[var].sel(PFT=10)
        ds['Shrub'] = ds[var].sel(PFT=11)+ds[var].sel(PFT=12)
        ds['C3G'] = ds[var].sel(PFT=11)
        ds['C4G'] = ds[var].sel(PFT=12)
        ds['C3Agr'] = ds[var].sel(PFT=13)+ds[var].sel(PFT=15)+ds[var].sel(PFT=16)+\
                      ds[var].sel(PFT=17)=ds[var].sel(PFT=20)+ds[var].sel(PFT=21)+
                      ds[var].sel(PFT=22)+ds[var].sel(PFT=25)
        ds['C4Agr'] = ds[var].sel(PFT=14)+ds[var].sel(PFT=18)+ds[var].sel(PFT=19)+\
                      ds[var].sel(PFT=23)+ds[var].sel(PFT=24)+ds[var].sel(PFT=26)
        ds['Other'] = ds[var].sel(PFT=13)+ds[var].sel(PFT=14)+\
                      ds[var].sel(PFT=15)+ds[var].sel(PFT=16)
        ds['Bare'] = xr.zeros_like(ds['EVG'])

    elif DGVM == 'LPX-Bern':
        decode_times=True
        '''
        1: Tropical broad evergreen
        2: Tropical broad raingreen
        3: Temperate needle evergreen
        4: Temperate broad evergeen;
        5: Temperate broad summergreen
        6: Boreal needle evergreen
        7: Boreal needle summergreen
        8: Boreal broad summergreen
        9; C3 herbaceous
        10: C4 herbaceous
        11: Peat graminoid
        12: Peat sphagnum moss
        13: Peat flood tolerant tropical broad evergeen
        14:Peat flood tolerant tropical broad raingreen
        15: Peat flood tolerant herbaceous
        16: Cropland C3 herbaceous
        17: Cropland C4 herbaceous;
        18: Pasture C3 herbaceous;
        19: Pasture C4 herbaceous
        20: Urban Bare;
        '''
        ds['EVG'] = ds[var].sel(PFT=1)+ds[var].sel(PFT=3)+ds[var].sel(PFT=4)+\
                    ds[var].sel(PFT=6)+ds[var].sel(PFT=13)
        ds['DCD'] = ds[var].sel(PFT=2)+ds[var].sel(PFT=5)+ds[var].sel(PFT=7)+\
                    ds[var].sel(PFT=8)+ds[var].sel(PFT=14)
        ds['Shrub'] = xr.zeros_like(ds['EVG'])
        ds['C3G'] = ds[var].sel(PFT=9)
        ds['C4G'] = ds[var].sel(PFT=10)
        ds['C3Agr'] = ds[var].sel(PFT=16)+ds[var].sel(PFT=18)
        ds['C4Agr'] = ds[var].sel(PFT=17)+ds[var].sel(PFT=19)
        ds['Other'] = ds[var].sel(PFT=20)
        ds['Bare'] = xr.zeros_like(ds['EVG'])

    elif DGVM == 'ORCHIDEE-CNP':
        decode_times=True
        '''
        Counting from 0 instead of 1
        1 bare land                          ",
        2 tropical broadleaf evergreen tree  ",
        3 tropical broadleaf deciduous tree  ",
        4 temperate needleleaf evergreen tree",
        5 temperate broadleaf evergreen tree ",
        6 temperate broadleaf deciduous tree ",
        7 boreal needleleaf evergreen tree   ",
        8 boreal broadleaf deciduous tree    ",
        9 boreal needleleaf deciduous tree   ",
        10 C3 grass                           ",
        11 C3 pasture                         ",
        12 C4 grass                           ",
        13 C4 pasture                         ",
        14 C3 agriculture                     ",
        15 C4 agriculture                     " ;
        '''
        ds['EVG'] = ds[var].sel(pft=1)+ds[var].sel(pft=3)+ds[var].sel(pft=4)+ \
                    ds[var].sel(pft=6)
        ds['DCD'] = ds[var].sel(pft=2)+ds[var].sel(pft=5)+ds[var].sel(pft=7)+\
                    ds[var].sel(pft=5)
        ds['Shrub'] = xr.zeros_like(ds['EVG'])
        ds['C3G'] = ds[var].sel(pft=9)
        ds['C4G'] = ds[var].sel(pft=11)
        ds['C3Agr'] = ds[var].sel(pft=10)+ds[var].sel(pft=13)
        ds['C4Agr'] = ds[var].sel(pft=12)+ds[var].sel(pft=14)
        ds['Other'] = xr.zeros_like(ds['EVG'])
        ds['Bare'] = ds[var].sel(pft=0)

    elif DGVM == 'ORCHIDEE':
        decode_times=True
        '''
        Counting from 0 instead of 1
        "PFT1: bare soil"
        "PFT2: tropical broadleaf evergreen"
        "PFT3: tropical broadleaf raingreen"
        "PFT4: temperate needleleaf evergreen"
        "PFT5: temperate broadleaf evergreen"
        "PFT6: temperate broadleaf summergreen"
        "PFT7: boreal needleleaf evergreen"
        "PFT8: boreal broadleaf summergreen"
        "PFT9: boreal needleleaf summergreen"
        "PFT10: temperate C3 grass"
        "PFT11: C4 grass"
        "PFT12: C3 agriculture"
        "PFT13: C4 agriculture"
        "PFT14: tropical C3 grass"
        "PFT15: boreal C3 grass
        '''
        ds['EVG'] = ds[var].sel(pft=1)+ds[var].sel(pft=3)+ds[var].sel(pft=4)+ \
                    ds[var].sel(pft=6)
        ds['DCD'] = ds[var].sel(pft=2)+ds[var].sel(pft=5)+ds[var].sel(pft=7)+\
                    ds[var].sel(pft=8)
        ds['Shrub'] = xr.zeros_like(ds['EVG'])
        ds['C3G'] = ds[var].sel(pft=9)+ds[var].sel(pft=13)+ds[var].sel(pft=14)
        ds['C4G'] = ds[var].sel(pft=10)
        ds['C3Agr'] = ds[var].sel(pft=11)
        ds['C4Agr'] = ds[var].sel(pft=12)
        ds['Other'] = xr.zeros_like(ds['EVG'])
        ds['Bare'] = ds[var].sel(pft=0)

    elif DGVM == 'SDGVM':
        decode_times=True
        '''
        1 BARE
        2 CITY
        3 C3
        4 C3crop
        5 C4
        6 C4crop
        7 Dc_Bl
        8 Dc_Nl
        9 Ev_Bl
        10 Ev_Nl
        '''
        ds['EVG'] = ds[var].sel(PFT=9)+ds[var].sel(PFT=10)
        ds['DCD'] = ds[var].sel(PFT=7)+ds[var].sel(PFT=8)
        ds['Shrub'] = xr.zeros_like(ds['EVG'])
        ds['C3G'] = ds[var].sel(PFT=3)
        ds['C4G'] = ds[var].sel(PFT=5)
        ds['C3Agr'] = ds[var].sel(PFT=4)
        ds['C4Agr'] = ds[var].sel(PFT=6)
        ds['Other'] = ds[var].sel(PFT=2)
        ds['Bare'] = ds[var].sel(PFT=1)

    elif DGVM == 'VISIT':
        decode_times=False
        '''
        "1: Tropical evergreen forest/woodland\n",
        "2: Tropical deciduous forest/woodland\n",
        "3: Temperate broadleaf evergreen forest/woodland\n",
        "4: Temperate needleleaf evergreen forest/woodland\n",
        "5: Temperate deciduous forest/woodland\n",
        "6: Boreal evergreen forest/woodland\n",
        "7: Boreal deciduous forest/woodland\n",
        "8: Evergreen/deciduous mixed forest/woodland\n",
        "9: Savanna\n",
        "10: Grassland/steppe\n",
        "11: Dense shrubland\n",
        "12: Open shrubland\n",
        "13: Tundra\n",
        "14: Desert\n",
        "15: Polar desert/rock/ice\n",
        "16: Cropland" ;
        '''
        ds['EVG'] = ds[var].sel(vegtype=1)+ds[var].sel(vegtype=3)+\
                    ds[var].sel(vegtype=4))+ds[var].sel(vegtype=6)
        ds['DCD'] = ds[var].sel(vegtype=2)+ds[var].sel(vegtype=5))+\
                    ds[var].sel(vegtype=7)
        ds['Shrub'] = ds[var].sel(vegtype=11)+ds[var].sel(vegtype=12)
        ds['C3G'] = ds[var].sel(vegtype=3)
        ds['C4G'] = ds[var].sel(vegtype=5)
        ds['C3Agr'] = ds[var].sel(vegtype=4)
        ds['C4Agr'] = ds[var].sel(vegtype=6)
        ds['Other'] = ds[var].sel(vegtype=8)+ds[var].sel(vegtype=9)+\
                      ds[var].sel(vegtype=13)
        ds['Bare'] = ds[var].sel(vegtype=14)+ds[var].sel(Pvegtype15)

    ds = ds.drop_vars(var)
    fname=('../landCoverFrac_S2_halfdegree/'+DGVM+'_S2_landCoverFrac.nc')

    ds.to_netcdf(fname,
                 encoding={'time':{'dtype': 'double'},
                           'latitude':{'dtype': 'double'},
                           'longitude':{'dtype': 'double'},
                           'landCoverFrac':{'dtype': 'float32'},
                           'EVG':{'dtype': 'float32'},
                           'DCD':{'dtype': 'float32'},
                           'Shrub':{'dtype': 'float32'},
                           'C3G':{'dtype': 'float32'},
                           'C4G':{'dtype': 'float32'},
                           'C3Agr':{'dtype': 'float32'},
                           'C4Agr':{'dtype': 'float32'},
                           'Other':{'dtype': 'float32'},
                           'Bare':{'dtype': 'float32'}})

   vegetation_groups('CABLE-POP')
