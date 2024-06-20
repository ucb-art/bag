import os
import pkg_resources

from bag.io.file import read_yaml

config_fname = pkg_resources.resource_filename(__name__, os.path.join('data', 'tech_params.yaml'))
config = read_yaml(config_fname)