#! /usr/bin/env python 

"""

Gemma Kulk - gku@pml.ac.uk, May 2026

TIME project - WP4 Uncertainties

Module of python code to compare in situ and satellite data for standardisation of statistical metrics for direct validation approach

Script calculates statistical metrics and then makes a scatter-density plot with histograms as an output

As input, a .csv file is needed with a column with in situ data and a column with satellite/model data

Statistical metrics that are calculated include:
- Number of observations,
- Bias,
- Root mean square difference,
- Centre-pattern root mean square difference,
- Slope of type-2 regression,
- Intercept of type-2 regression, and
- Correlation coefficient,

and are further described in Brewin *et al.* (2015), https://doi.org/10.1016/j.rse.2013.09.016

"""


##### Import libraries
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


##### Define functions

# Calculation of statistics 
def stat_metrics(in_situ, model, log_transformed):
    
    # Carry out statistical analysis 
    
    # Apply pearson correlation for log-transformed data
    if log_transformed == True:
        r, p = pearsonr(in_situ, model) 
    
    # Apply spearman correlation for untransformed data
    else:
        r, p = spearmanr(in_situ, model) 
    
    # Obtain number of observations
    n = len(in_situ) 
    
    # Obtain bias
    bias = np.mean(model - in_situ)
    
    # Obtain root mean square difference
    rmsd = np.sqrt(mean_squared_error(in_situ, model)) 
    
    # Obtain centre-pattern root mean square difference
    cp_rmsd = np.sqrt(np.mean((model - np.mean(model) - (in_situ - np.mean(in_situ)))** 2)) 

    # Return data
    return n, r, p, bias, rmsd, cp_rmsd

# Type 2 regression analysis
def type2_regression(in_situ, model, r):
    
    # Fit regression
    
    # Obtain slope
    s = np.std(model) / np.std(in_situ) * np.sign(r) 
    
    # Obtain intercept
    i = np.mean(model) - s * np.mean(in_situ) 
    
    # Obtain r-squared
    r2 = r**2 
    
    # Return data
    return s, i, r2
    
    
    
    
       
        