# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:30:04 2022

@author: alumno
"""

def suma_dig (n):
    if n == 0:
        return 0
    return suma_dig(n//10) + n%10 

print(suma_dig(450))