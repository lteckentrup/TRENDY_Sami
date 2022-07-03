## Check grid and time steps
# declare -a DGVM_list=('CABLE-POP' 'CLASS-CTEM' 'CLM5.0' 'DLEM' 'ISBA-CTRIP' 
#                       'JSBACH' 'JULES-ES' 'LPJ-GUESS' 'LPX-Bern' 'OCN' 
#                       'ORCHIDEE-CNP' 'ORCHIDEE' 'SDGVM' 'VISIT'

# for DGVM in "${DGVM_list[@]}"; do
    # echo ${DGVM}
    # cdo griddes ${DGVM}_S2_gpp.nc
    # cdo ntime landCoverFrac_S2/${DGVM}_S2_landCoverFrac.nc
# done

# ------------------------------------------------------------------------------

### Files have weird chunking/ dimension orders and need to be reorganised.
### Has to be submitted as job
# nccopy -c 'time/1,lat/,lon/' gpp_S2/DLEM_S2_gpp.nc \
#                              gpp_S2/DLEM_S2_gpp_chunks.nc
# ncpdq -F -O -a time,PFT,latitude,longitude gpppft_S2/LPJ-GUESS_S2_gpppft.nc \
#                                            gpppft_S2/LPJ-GUESS_S2_gpppft_reorder.nc
# ncpdq -F -O -a time,PFT,latitude,longitude gpppft_S2/LPX-Bern_S2_gpppft.nc \
#                                            gpppft_S2/LPX-Bern_S2_gpppft_reorder.nc

### DGVMs with coarse grid
declare -a DGVM_list_coarse=('CABLE-POP' 'CLASS-CTEM'  'CLM5.0' 'ISBA-CTRIP'
                             'JSBACH' 'JULES-ES' 'OCN' 'ORCHIDEE-CNP' 'SDGVM')

### DGVMs with half degree grid
declare -a DGVM_list_fine=('DLEM' 'LPJ-GUESS' 'LPX-Bern' 'ORCHIDEE'
                           'VISIT')


### First order conservative remapping for coarse models, select years 1901-2018
for DGVM in "${DGVM_list_coarse[@]}"; do
    if [ ${DGVM} = JSBACH ]; then
         echo ${DGVM}
         cdo -L -remapycon,halfdegree.txt -sellonlatbox,-180,180,-90,90 \
                landCoverFrac_S2/${DGVM}_S2_landCoverFrac.nc \
                landCoverFrac_S2_halfdegree/${DGVM}_S2_landCoverFrac.nc
    elif [ ${DGVM} = CLM5.0 ]; then
         echo ${DGVM}
         cdo -L -remapycon,halfdegree.txt -sellonlatbox,-180,180,-90,90 \
                -sellevel,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,42,43,62,63,68,69,76,77,78,79 \
                landCoverFrac_S2/${DGVM}_S2_landCoverFrac.nc \
                landCoverFrac_S2_halfdegree/${DGVM}_S2_landCoverFrac.nc
    elif [ ${DGVM} = CABLE-POP ]; then
         echo ${DGVM}
         cdo -L -remapycon,halfdegree.txt -sellonlatbox,-180,180,-90,90 \
                -selyear,1901/2018 -yearmean -delvar,latitude_2,longitude_2 \
                landCoverFrac_S2/${DGVM}_S2_landCoverFrac.nc \
                landCoverFrac_S2_halfdegree/${DGVM}_S2_landCoverFrac.nc
    elif [ ${DGVM} = ISBA-CTRIP ]; then
         echo ${DGVM}
         cdo -L -remapycon,halfdegree.txt -sellonlatbox,-180,180,-90,90 \
                -selyear,1901/2018 -yearmean -chname,lCoverFrac,landCoverFrac \
                landCoverFracS2/${DGVM}_S2_landCoverFrac.nc \
                landCoverFrac_S2_halfdegree/${DGVM}_S2_landCoverFrac.nc
    else
         echo ${DGVM}
         cdo -L -remapycon,halfdegree.txt -sellonlatbox,-180,180,-90,90 \
                -selyear,1901/2018 \
                 landCoverFrac_S2/${DGVM}_S2_landCoverFrac.nc \
                 landCoverFrac_S2_halfdegree/${DGVM}_S2_landCoverFrac.nc
    fi
done

### Harmonize grid for fine res DGVMs (might not be necessary)
for DGVM in "${DGVM_list_fine[@]}"; do
    if [ ${DGVM} = VISIT ]; then
         echo ${DGVM}
         cdo -L -remapycon,halfdegree.txt -sellonlatbox,-180,180,-90,90 \
                landCoverFrac_S2/${DGVM}_S2_landCoverFrac.nc \
                landCoverFrac_S2_halfdegree/${DGVM}_S2_landCoverFrac.nc
    elif [ ${DGVM} = LPX-Bern ] || [ ${DGVM} = ISBA-CTRIP ]; then
         echo ${DGVM}
         cdo -L -sellonlatbox,-180,180,-90,90 -selyear,1901/2018 -yearmean \
                landCoverFrac_S2/${DGVM}_S2_landCoverFrac.nc \
                landCoverFrac_S2_halfdegree/${DGVM}_S2_landCoverFrac.nc
    else
         echo ${DGVM}
         cdo -L -sellonlatbox,-180,180,-90,90 -selyear,1901/2018 \
                 landCoverFrac_S2/${DGVM}_S2_landCoverFrac.nc \
                 landCoverFrac_S2_halfdegree/${DGVM}_S2_landCoverFrac.nc
    fi
done

### First order conservative remapping for coarse models, select years 1901-2018
for DGVM in "${DGVM_list_coarse[@]}"; do
    for var in gpp gpppft lai; do
        echo ${var}
        if [ ${DGVM} = ISBA-CTRIP ]; then
            echo ${DGVM}
            cdo -L -remapycon,halfdegree.txt -sellonlatbox,-180,180,-90,90 \
                   -settaxis,1901-01-01,00:00,1month -selyear,1901/2018 \
                   ${var}_S2/${DGVM}_S2_${var}.nc \
                   ${var}_S2_halfdegree/${DGVM}_S2_${var}.nc
         elif [ ${DGVM} = CABLE-POP ]; then
             echo ${DGVM}
             cdo -L -remapycon,halfdegree.txt -sellonlatbox,-180,180,-90,90 \
                    -selyear,1901/2018 -delvar,latitude_2,longitude_2 \
                    ${var}_S2/${DGVM}_S2_${var}.nc \
                    ${var}_S2_halfdegree/${DGVM}_S2_${var}.nc
          else
            echo ${DGVM}
            cdo -L -remapycon,halfdegree.txt -sellonlatbox,-180,180,-90,90 \
                   -selyear,1901/2018 ${var}_S2/${DGVM}_S2_${var}.nc \
                   ${var}_S2_halfdegree/${DGVM}_S2_${var}.nc
          fi
    done
done

### Select years for fine res DGVMs
for DGVM in "${DGVM_list_fine[@]}"; do
  for var in gpp gpppft lai; do
        echo ${DGVM}
        echo ${var}
        if [ ${DGVM} = DLEM ] || [ ${DGVM} = VISIT ]; then
             cdo -L -invertlat -sellonlatbox,-180,180,-90,90 -selyear,1901/2018 \
                    ${var}_S2/${DGVM}_S2_${var}.nc \
                    ${var}_S2_halfdegree/${DGVM}_S2_${var}.nc
        else
             cdo -L -sellonlatbox,-180,180,-90,90 -selyear,1901/2018 \
                    ${var}_S2/${DGVM}_S2_${var}.nc \
                    ${var}_S2_halfdegree/${DGVM}_S2_${var}.nc
        fi
    done
done
