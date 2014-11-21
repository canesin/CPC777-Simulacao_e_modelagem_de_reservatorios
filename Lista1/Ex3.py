# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 22:39:15 2014

@author: Fabio
"""
from pint import UnitRegistry
import numpy as np
from math import cos, pi
from sympy.mpmath import mp, nsum, inf

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

mp.dps = 25
mp.pretty = True
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
d = _Q(2000, 'ft')


size = 50

XX, YY = np.mgrid[0:d.magnitude:complex(0, size),
                  0:d.magnitude:complex(0, size)]
Pressure = np.empty((size, size))
dmag = d.magnitude


def somando(x, y, r, s):
    return (cos((2*r + 1)*pi)*x/dmag)*(cos((2*s + 1)*pi)*y/dmag)/((2*r + 1)**2 + (2*s + 1)**2)

for i in xrange(size):
    for j in xrange(size):
        somatorio = nsum(lambda ri, si: somando(XX[i, j], YY[i, j], ri, si),
                         [0, inf], [0, inf], maxterms=30)
        pres = Pi - (16. / pi**2) * ((muo * qo_std * Bo) / (k * h)) * somatorio
        Pressure[i, j] = pres.magnitude

fig1 = plt.figure()
fig1.patch.set_facecolor('white')
plt.rcParams['legend.loc'] = 'best'

plt.title(u'Pressão em curvas de nível - padrão five-spot')
plt.xlabel(u'x [ft]')
plt.ylabel(u'y [ft]')
pressure_levels = np.linspace(500, 2200, 9).tolist()
CS = plt.contour(XX, YY, Pressure, levels=pressure_levels, colors='k')
plt.clabel(CS, fmt='%.1f', fontsize=12, inline=1)
