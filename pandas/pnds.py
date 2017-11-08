#!/usr/bin/env python3.5


import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_pdf import PdfPages


x = pd.read_csv('file.csv', na_values={'Last Name': ['.', 'NA'], 'Pre-Test Score': ['.']})

a = x['age']
print(a)

b = x['postTestScore']
print(b)


#do souboru
f = plt.figure()
plt.plot(a)
f.savefig('age.pdf')

#plt.show(b.plot())
