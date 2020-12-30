# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:28:39 2020

@author: Julian
"""

from Caeser import caesar
from Scalar import scalar

def test_caesar():
    assert caesar("Hslh qhjah lza",7) == print("ALEA JACTA ESE")

def test_scalar():
    return scalar([1,2],[1,2]) == 4

