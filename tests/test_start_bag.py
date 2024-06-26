# TODO: in pytest 7, this can be moved to pytest.ini
import sys  
sys.path.append('src')
sys.path.append('pybag/_build/lib')
sys.path.append('tests')

# These are all necessary for BagProject initialization
# TODO: I could use a fixture to add these
import os
cwd = os.getcwd()
os.environ['BAG_TECH_CONFIG_DIR'] = f'{cwd}/tests/util/'
os.environ['BAG_CONFIG_PATH'] = f'{cwd}/tests/util/bag_config.yaml'
os.environ['BAG_WORK_DIR'] = f'{cwd}/tmp'
os.environ['BAG_TEMP_DIR'] = f'{cwd}/tmp'

from bag.core import BagProject
from bag.util.misc import register_pdb_hook

register_pdb_hook()

def test_startup() -> bool:
    # Test if we can successfully start a BagProject, the main entry point into BAG
    # This includes loading pybag and setting up the mock tech librayr.
    prj = BagProject()
    return 1
