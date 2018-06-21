"""calculateTemp.py -- Fitting a blackboady curve on a G0 star of ~6000 K
Final project solution for 2018 REU 

NAME
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import h,k,c
