"""What is SciPy?
SciPy is a scientific computation library that uses NumPy underneath.

SciPy stands for Scientific Python.

It provides more utility functions for optimization, stats and signal processing.

Like NumPy, SciPy is open source so we can use it freely.

SciPy was created by NumPy's creator Travis Olliphant.


Why Use SciPy?
If SciPy uses NumPy underneath, why can we not just use NumPy?

SciPy has optimized and added functions that are frequently used in NumPy and Data Science.


Which Language is SciPy Written in?
SciPy is predominantly written in Python, but a few segments are written in C.

import SciPy
Once SciPy is installed, import the SciPy module(s) you want to use in your applications by adding the from scipy import module statement:



"""
"""Checking SciPy Version
The version string is stored under the __version__ attribute."""
import scipy
print(scipy.__version__)

#Constants in SciPy
from scipy import constants
print(constants.pi)

#Constant Units
from scipy import constants
print(dir(constants))

"""Unit Categories
The units are placed under these categories:

Metric
Binary
Mass
Angle
Time
Length
Pressure
Volume
Speed
Temperature
Energy
Power
Force"""

"""Metric (SI) Prefixes:
Return the specified unit in meter (e.g. centi returns 0.01)"""
from scipy import constants
print(constants.yotta)
print(constants.yotta)    #1e+24
print(constants.zetta)    #1e+21
print(constants.exa)      #1e+18
print(constants.peta)     #1000000000000000.0
print(constants.tera)     #1000000000000.0
print(constants.giga)     #1000000000.0
print(constants.mega)     #1000000.0
print(constants.kilo)     #1000.0
print(constants.hecto)    #100.0
print(constants.deka)     #10.0
print(constants.deci)     #0.1
print(constants.centi)    #0.01
print(constants.milli)    #0.001
print(constants.micro)    #1e-06
print(constants.nano)     #1e-09
print(constants.pico)     #1e-12
print(constants.femto)    #1e-15
print(constants.atto)     #1e-18
print(constants.zepto)    #1e-21

"""Binary Prefixes:
Return the specified unit in bytes (e.g. kibi returns 1024)"""
from scipy import constants

print(constants.kibi)    #1024
print(constants.mebi)    #1048576
print(constants.gibi)    #1073741824
print(constants.tebi)    #1099511627776
print(constants.pebi)    #1125899906842624
print(constants.exbi)    #1152921504606846976
print(constants.zebi)    #1180591620717411303424
print(constants.yobi)    #1208925819614629174706176
