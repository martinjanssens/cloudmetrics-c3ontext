import xarray as xr

def ds_date_mean(ds):
    keys = [i for i in ds.data_vars]
    for i in range(len(keys)):
        if i == 0:
            ds_date = ds[keys[i]].groupby('date.date').mean()
        else:
            ds_date = xr.merge([ds_date, ds[keys[i]].groupby('date.date').mean()])
    return ds_date

