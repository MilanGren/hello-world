#!/usr/bin/env python3.5


import platform
print("%-s %-s" % ("verze je",platform.python_version()))

import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)