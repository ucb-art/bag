# Manual run script to sanity check test_start_bag.py

import sys  
sys.path.append('src')
sys.path.append('pybag/_build/lib')
sys.path.append('tests')

import os
cwd = os.getcwd()
os.environ['BAG_TECH_CONFIG_DIR'] = f'{cwd}/tests/util/'
os.environ['BAG_CONFIG_PATH'] = f'{cwd}/tests/util/bag_config.yaml'
os.environ['BAG_WORK_DIR'] = f'{cwd}/tmp'
os.environ['BAG_TEMP_DIR'] = f'{cwd}/tmp'

from bag.core import BagProject
from bag.util.misc import register_pdb_hook

register_pdb_hook()

if __name__ == '__main__':
    print(f"Python sys path: {sys.path}")
    print(f"Checking directories...")
    print('pybag', os.listdir("pybag"))
    print('pybag/_build', os.listdir("pybag/_build"))
    print('Trying to import pybag')
    import pybag
    print('creating BAG project')
    _prj = BagProject()
