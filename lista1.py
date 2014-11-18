# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 22:39:15 2014

@author: Fabio
"""


from pint import UnitRegistry
from math import pi

ureg = UnitRegistry()
_Q = ureg.Quantity

phi = 0.2
c_t = _Q(1.5e-05, '1/psi')
k = _Q(150, 'mdarcy')
h = _Q(10, 'ft')
qo_std = _Q(3000, '1/day')
Bo = _Q(1.5, 'bbl')
muo = _Q(0.33, 'cpoise')
Pi = _Q(2200, 'psi')
rw = _Q(3.5, 'in')
re = _Q(2000, 'ft')


# Pd = ((2 * pi * k * h)/(qo_std * Bo * muo)) * (Pi - P)

def td(t):
    return (k * t)/(phi * muo * c_t * (rw**2))


def rd(r):
    return r/rw

times = [_Q(1, 'min'), _Q(1 , 'hour'), _Q(1, 'day'),
         _Q(30, 'day'), _Q(1, 'year'), _Q(10, 'year')]

Pressures = []
for time in times:
    Pressures.append( 0.5 * E)