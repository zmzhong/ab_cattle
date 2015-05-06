#!/usr/bin/python -tt
#==============================================================================
#                            General Documentation

"""Define tests for unittest for module cattle in the ab_cattle package.

   Execution of:
   $ python test.py

   in this tests directory will execute all tests, including those defined 
   in this current module.

   This module contains a single class named Tests.  This class consists
   solely of methods that are tests.  Global data initialization is done
   in test.py.
"""

#------------------------------------------------------------------------------
#                           Additional Documentation
#
# RCS Revision Code:
#   $Id: test_exam.py 64 2008-11-13 18:47:45Z jlin $
#
# Modification History:
# - 5 May 2015:  Adapted for cattle and disease package.
# - 16 Mar 2006:  Original by Johnny Lin, Physics Department, North Park 
#   University.
#
# Notes:
# - Written for Python 2.7.
# - See import/reload statements throughout module for dependencies.
#
# Copyright (c) 2006-2015 by Johnny Lin.  For licensing, distribution 
# conditions, contact information, and additional documentation see
# the URL http://www.johnny-lin.com/pylib.shtml.
#==============================================================================




#------------------- Module General Import and Declarations -------------------

#- If you're importing this module in testing mode, append the directory
#  the package is in to the PYTHONPATH so imports to the package can be
#  resolved.  See:  http://stackoverflow.com/a/19190695.

import os
if (__name__ == '__main__') and (__package__ is None):
    filename = os.path.abspath(__file__)
    tests_dir = os.path.dirname(filename)
    package_dir = os.path.dirname(tests_dir)
    parent_to_package_dir = os.path.dirname(package_dir)
    os.sys.path.append(parent_to_package_dir)


#- Import other modules at module level:

import copy
import matplotlib.pyplot as plt
import numpy as N
from ab_cattle import cattle
from ab_cattle import farm
from ab_cattle import visualize




#------------------------------------ Tests -----------------------------------

class Tests(object):
    def test_make_plot_of_farm(self):
        aFarm = farm.Farm()
        list_of_cattle = []

        for i in range(10):
            xloc = N.random.randint(aFarm.width)
            yloc = N.random.randint(aFarm.length)
            temp_cattle = cattle.Cattle( x_init=xloc, 
                                         y_init=yloc,
                                         env=aFarm )
            temp_cattle.state = "Recovered"
            list_of_cattle.append(temp_cattle)

        visualize.plot_farm(aFarm, list_of_cattle, show=True)
        #plt.plot([1,2,3,4], [3,4,5,2])
        #plt.show()




# ===== end file =====
