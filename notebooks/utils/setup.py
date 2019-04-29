# @Author: Maxime Caïtucoli <mcaitucoli>
# @Date:   2019-04-29T16:58:00+08:00
# @Last modified by:   mcaitucoli
# @Last modified time: 2019-04-29T20:36:25+08:00

from .imports import *
from .paths import *

try:
    get_ipython().magic('load_ext autoreload')
    get_ipython().magic('autoreload 2')
    get_ipython().magic('matplotlib notebook')
except NameError:
    pass

pd.set_option('display.max_columns', None)
