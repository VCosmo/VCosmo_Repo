This repository contains the data, results and code distribution for Physics Laboratory II experience "Virgo_DA_cosmo: Study of the systematics due to galaxies’ intrinsic luminosity for gravitational wave cosmology".

To run the notebooks you will need a working copy of Python3 with standard packages such as numpy and scipy.

# Short description of the content

- gal4H0_luminosity.py : Python module from https://github.com/simone-mastrogiovanni/hitchhiker_guide_dark_sirens , for simulating mock data and calculating the likelihood as function of H0. Some functions are updated to the the case in which we have a non negligible intrinsic luminosity dependence.

- H0analysis.ipynb : Do the analysis for various number of GW events exploring different cases for the GW likelihood. It extracts the mean value for H0 and the interval that contains 68% area of the posterior.

- run_data.ipynb : generate a number Nrep of posteriors on H0 for three different assumptions on the intrinsic luminosity dependence.

- ppplots.ipynb: It produces the PP-plots (Parameter-Parameter plots). Unfortunately git does not have the possibility of storing very heavy files. To produce the files needed for this notebook, you will need to run the python script run_data.ipynb .
