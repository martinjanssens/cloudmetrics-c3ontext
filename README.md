# cloudmetrics-c3ontext
Attempt to marry [cloudmetrics](https://github.com/cloudsci/cloudmetrics), a package to compute metrics of the organisation of 2D cloud fields, to [C3ONTEXT](https://github.com/observingClouds/C3ONTEXT), a data set of satellite-observed cloud scenes and their human classification into pattern classes.
The code is under development, and currently consists of:
- A notebook of early analysis by Marion Dugué
- Martin's add-on notebook, which currently loops over a few files underlying C3ONTEXT, computes the following metrics for each scene and stores them in a `pandas DataFrame`, `df_metrics`:

```
metrics = ['cloud_fraction',
           'fractal_dimension',
           'open_sky',
           'cop',
           'iorg',
           'scai',
           'max_length_scale',
           'mean_eccentricity',
           'mean_length_scale',
           'mean_perimeter_length',
           'num_objects',
           'orientation',
           'spectral_length_moment',
           'spectral_anisotropy',
           'spectral_slope',
           'woi1',
           'woi2',
           'woi3'
          ]
```

Later commits will:
1. Extend the computation to all scenes
2. Include more scalar metrics
3. Add postprocessing of `df_metrics` that allows computation of prinicipal components
4. Integrate the results with C3ONTEXT
