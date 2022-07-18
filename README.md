# cloudmetrics-c3ontext
Attempt to marry [cloudmetrics](https://github.com/cloudsci/cloudmetrics), a package to compute metrics of the organisation of 2D cloud fields, to [C3ONTEXT](https://github.com/observingClouds/C3ONTEXT), a data set of satellite-observed cloud scenes and their human classification into pattern classes.
The code is under development, and currently consists of:
- A notebook of early analysis by Marion Dugué (`marion.ipynb`)
- Martin's reinterpretation of that notebook (`cloudmetrics-goes16-IR.ipynb`), which currently loops over the files underlying C3ONTEXT, computes the metrics listed below for each scene and stores them in a `pandas DataFrame`, `df_metrics`:
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
           'woi3',
           'mean',
           'var'
          ]
```
- A comparison to the level-3, 'instant'-sampled, manually classified IR images in `C3ONTEXT` (`level3_IR_instant`), in an attempt to reproduce fig. 6 from [Schulz (2022)](https://doi.org/10.5194/essd-14-1233-2022) (`compare-C3ONTEXT.ipynb`).

Currently I am attempting to add a few analyses of personal interest, e.g.:
- Do pattern classes cover larger areas of scenes as you move towards the fringes of the distribution? I.e. how extreme are they, and how representative are combinations of pattern classes of any point in the metric space (see `compare-C3ONTEXT.ipynb`)?
- Do we see typical trajetories through metric space?

> **NOTE**: The level-3 c3ontext data should be accessible through the `eurec4a` catalag, but I am currently unable to make that work  (see https://github.com/eurec4a/eurec4a-intake/issues/106), and so have downloaded the data myself from https://zenodo.org/record/5979718#.Yrxu2hNBztM
