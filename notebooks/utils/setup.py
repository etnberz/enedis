# @Author: Maxime Caïtucoli <mcaitucoli>
# @Date:   2019-04-29T16:58:00+08:00
# @Last modified by:   maxime
# @Last modified time: 2019-05-02T16:06:36+08:00

from .imports import *
from .paths import *
from .constants import *
from .plots import *

try:
    get_ipython().magic('load_ext autoreload')
    get_ipython().magic('autoreload 2')
    get_ipython().magic('matplotlib notebook')
except NameError:
    pass

pd.set_option('display.max_columns', None)
