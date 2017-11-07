#!/usr/bin/env python3.5

import platform
print("%-s %-s" % ("verze je",platform.python_version()))





import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)


from numpy import pi
print(np.linspace( 0, 2, 9 ))