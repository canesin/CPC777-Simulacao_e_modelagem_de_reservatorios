# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 22:39:15 2014

@author: Fabio
"""
from pint import UnitRegistry
from matplotlib import pylab as pl
import numpy as np
from sympy import pi, cos, symbols
from sympy.mpmath import mp, nsum, inf


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


XX, YY = np.mgrid[0:d.magnitude:100j, 0:d.magnitude:100j]
Pressure = np.empty((100, 100))
dmag = d.magnitude


def somando(x, y, r, s):
    return (cos((2*r + 1)*pi)*x/dmag)*(cos((2*s + 1)*pi)*y/dmag)/((2*r + 1)**2 + (2*s + 1)**2)

for i in xrange(100):
    for j in xrange(100):
        somatorio = nsum(lambda ri, si: somando(XX[i, j], YY[i, j], ri, si), [0, inf], [0, inf])
        pres = Pi - (16. / pi**2) * ((muo * qo_std * Bo) / (k * h)) * somatorio
        Pressure[i, j] = pres.magnitude

#
#fig1 = pl.figure()
#fig1.patch.set_facecolor('white')
#pl.rcParams['legend.loc'] = 'best'
#for idx, timestep in enumerate(Pressures):
#    pl.title(u'Pressão no fundo do poço - $P_{wf}$')
#    pl.xlabel(u'Tempo [sec]')
#    pl.ylabel(u'Pressão [psi]')
#    pl.plot(times,
#            [pressure.to('psi').magnitude for pressure in timestep],
#            label=Ss[idx])
#    pl.legend()
