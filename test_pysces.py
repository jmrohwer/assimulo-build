#!/usr/bin/env python3

import pysces
print('PySCeS version:', pysces.__version__)
pysces.test(3)

m = pysces.model('pysces_test_linear1')
print("LSODA")
m.doSim()
print('CVODE')
m.mode_integrator = 'CVODE'
m.doSim()

