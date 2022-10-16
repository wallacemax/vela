__author__ = 'maxwallace'
import sys
import datetime
import os
import numpy
import pandas as pd
import seaborn as sb

import pickle

import matplotlib
from utils import *

class VELA_Main():

    def __init__(self, master):
        self.master = master
        
    #https://physics.nist.gov/PhysRefData/XrayMassCoef/ElemTab/z07.html

    #get data from vela graphs
        #vela 6911 747 YCA, YVA
        #vela 6909 747 YCA, YVA
        #vela 6911 FR YCA, YVA
        #vela 6909 FR YCA, YVA
        
    def get_df_from_csv(filename, df_file):
        df_file = pd.read_csv(filename);
        
    self.df_signal_data = [];
    self.df_attenuation_constants = [];
    
    def get_attenuation_constants(df_attenuation_constants):
        
    
    def get_datasets():
        
        


    #get length of path b/w ocean surface and VELA

        #TODO: get the real orbital distance

    #determine some guess for factor between yield and amplitude

    #find the missing energy as a function of elemental percentage and hope it's steel?




