#!/usr/bin/env python3

import os
import sysconfig
import glob
import subprocess

EX_PATH = os.path.join(sysconfig.get_path('platlib'), 'assimulo', 'examples')
os.chdir(EX_PATH)

CVODE_EXAMPLES = glob.glob('cvode*.py')
print('Examples:')
print(CVODE_EXAMPLES)
print(' ')

for file in CVODE_EXAMPLES:
    subprocess.run(["python3", file])

