# STVC-LG_paper
Paper "PM2.5 estimation and its relationship with NO2 and SO2 in China from 2016 to 2020" (Doi:10.1080/17538947.2024.2398055) Experimental reproduction archive.

## Description
Only the 1st-5th January 2020 example CSV data are provided here due to the excessive size of the experimental raw data and remote sensing imagery data.
The generated daily 1 km PM2.5 distribution (in China from 2016-2020) is available in Zenodo at https://doi.org/10.5281/zenodo.11145467.  
For more information about the paper and the STVC-LG model in detail, please get in touch with Huangyuan Tan (tanhuangyuan@whu.edu.cn)

### (1)./csv_data/china_pm25_2020_xev.csv
- stationID: monitoring station ID
- time: e.g., 20200101 represents 1st Jan 2020
- pm: pm2.5 concentration value
- lon: longitude
- lat: latitude
- aod: aerosol optical depth
- blh: boundary layer height
- ps: surface pressure
- rh: relative humidity
- temp: surface temperature
- u: 10m wind speed u-component
- v: 10m wind speed v-component
- ndvi: normalized difference vegetation index
- dem: elevation
- pop: population density
- barren: barren landcover type density
- city: city landcover type density
- farm: farm landcover type density
- green: vegetation landcover type density
- water: water landcover type density
- ev1-ev8: spatial eigenvector 1-8
- x_evn: spatial interaction term between "x" and "evn", e.g., "aod_ev1" represents spatial interaction term between "aod" and "ev1"
- doy: day of the year
- month: month index

### (2)./selection_proc/variables_pm25.csv
The selected variables.

### (3)./model_proc.py
The main executable file.
Due to the limit of package "Autogluon", the saving path must be an absolute path.
You may change the path.
`save_path_pm25 = 'D:/stsvc_pm25_model'`

## Environment requirements
Python 3.8; Autogluon 0.7.0
