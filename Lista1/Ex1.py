# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 22:39:15 2014

@author: Fabio
"""
from pint import UnitRegistry
from sympy import Ei
from matplotlib import pylab as pl
import numpy as np
from math import pi, log

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


def P_f(Pd):
    return Pi + (((qo_std * Bo * muo)/(2 * pi * k * h)) * Pd)


def td_f(t):
    return ((k * t)/(phi * muo * c_t * (rw**2))).to('dimensionless')


def rd_f(r):
    return (r/rw).to('dimensionless')

times = [_Q(1, 'min'), _Q(1 , 'hour'), _Q(1, 'day'),
         _Q(30, 'day'), _Q(1, 'year'), _Q(10, 'year')]

rd = rd_f(_Q(np.linspace(rw.to('in').magnitude,
                         re.to('in').magnitude, 100), 'in'))

td = map(td_f, times)

Pressures = []
for time in td:
    values = []
    for radius in rd:
        values.append(P_f(0.5 * Ei(-radius**2/(4 * time)).n(chop=True)))
#        values.append(P_f(0.5 * log(1.781*radius**2/(4 * time))))
    Pressures.append(values)

fig1 = pl.figure()
fig1.patch.set_facecolor('white')
pl.rcParams['legend.loc'] = 'best'
for idx, timestep in enumerate(Pressures):
    pl.title(u'Perfil radial de pressão no reservatório')
    pl.xlabel(u'Raio [ft]')
    pl.ylabel(u'Pressão [psi]')
    pl.plot(np.linspace(rw.to('ft').magnitude, re.to('ft').magnitude, 100),
            [pressure.to('psi').magnitude for pressure in timestep],
            label=times[idx])
    pl.legend()
