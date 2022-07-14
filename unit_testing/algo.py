# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 12:20:56 2022

@author: aspdi
"""

import pytest
 
def area_of_rectangle(width, height):
    area = width*height
    return area
 
def perimeter_of_rectangle(width, height):
    perimeter = 2 * (width + height)
    return perimeter