# low-temperature-electrolyte-conductivity
This repository describes my efforts to improve predictions for electrolyte conductivity in Li-ion batteries at low temperatures, building on the efforts of an EU BIGMAP publication (Flores et al., Digital Discovery, 2022)
## Motivation
The work of Flores et al. (2022) developed a symbolic regression model to predict electrolyte conductivity as a function of temperature, salt loading and fraction of propylene carbonate in the electrolyte. This study is an effort to improve the authors' findings at low temperatures ( 243 K), using these approaches
1. create symbolic regression features specifically for 243 K using AutoFeat
2. use altered weights for existing features from Flores et al. (2022) using linear regression, using CV grid search, ridge and lasso techniques to find the optimum 
    regularization parameters
3. Fitting a 4th degree polynomial in salt loading using the MATLAB curve fitting toolbox.

### Data cleanup
Prior to fitting, the raw data had to be cleaned up by averaging multiple experimental runs. 

## Available ppts
The entire workflow is described in the "Low Temperature Correction" deck.

## Available scripts
This repository has the following scripts:
1. MATLAB code to clean up and process raw data to make it model-ready
2. MATLAB curve fitting app results
3. Feature generation code in Python for low temperarure using AutoFeat
4. Linear regression code in Python to generate altered weights to Flores et al. (2022) along with grid search for identifying optimum regularization parameters

Here is the github profile for the BIGMAP study: https://github.com/BIG-MAP/SR-electrolytes, while the link to the Flores et al. (2022) paper is here: https://pubs.rsc.org/en/content/articlelanding/2022/DD/D2DD00027J


