#!/usr/bin/env python3

import platform

print("%-s %-s" % ("verze je",platform.python_version()))

ary = ['orange', 'apple', 'pear', 'banana', 'kiwi']

print(ary.index('kiwi'))

items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in items: #enumerate(items):
  print(item)

nove = [1,2,None,3,0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i,item in enumerate(items):
  nove[i] = item
      
print(nove)

a = [1, 9, 8, 4]
a = [elem*2+index for index,elem in enumerate(a)] 
#b = a
#b = [elem*2+index for index,elem in enumerate(li)] 


print(a)