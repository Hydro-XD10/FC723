# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 08:30:54 2024

@author: hydro
"""


import the_euclidean_algorithm_code_refactored as ss

def test_find_the_greatest_common_factor():
    GCD= ss.Math.find_the_greatest_common_factor(0, 3)
    assert GCD== 3, "The greatest common factor"