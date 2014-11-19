# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 22:39:15 2014

@author: Fabio
"""
from pint import UnitRegistry
from matplotlib import pylab as pl
import numpy as np
from math import pi, log, exp

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
gamma = 1.78108
Ss = [-5, -2, 0, 2, 5]


def P_f(Pd):
    return Pi - (((qo_std * Bo * muo)/(2 * pi * k * h)) * Pd)


def td_f(t):
    return ((k * t)/(phi * muo * c_t * (rw**2))).to('dimensionless')


times = _Q(np.linspace(1e-3, 10e3, 100), 'second')

td = td_f(times)

Pressures = []
for S in Ss:
    values = []
    for time in td:
        values.append(P_f(0.5 * log(4 * time/(gamma * exp(-2*S)))))
    Pressures.append(values)

fig1 = pl.figure()
fig1.patch.set_facecolor('white')
pl.rcParams['legend.loc'] = 'best'
for idx, timestep in enumerate(Pressures):
    pl.title(u'Pressão no fundo do poço - $P_{wf}$')
    pl.xlabel(u'Tempo [sec]')
    pl.ylabel(u'Pressão [psi]')
    pl.plot(times,
            [pressure.to('psi').magnitude for pressure in timestep],
            label=Ss[idx])
    pl.legend()
