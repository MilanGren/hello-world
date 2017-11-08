#!/usr/bin/env python3

import platform
print("%-s %-s" % ("verze je",platform.python_version()))



import scipy.io as sio
m = sio.loadmat('cross_sections.mat')
print(m.keys)




#import numpy as np
#import h5py 
#f = h5py.File('cross_sections.mat','r')


#import h5py 
#f = h5py.File('serpent_input_1_det0.m','r') 

