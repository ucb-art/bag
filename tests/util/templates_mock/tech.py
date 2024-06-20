# -*- coding: utf-8 -*-
from bag.layout.tech import TechInfo

from . import config as _config
from . import config_fname as _config_fname

class TechInfoMock(TechInfo):
    def __init__(self, process_params):
        TechInfo.__init__(self, process_params, _config, _config_fname)

