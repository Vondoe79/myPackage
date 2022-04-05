# import modules, packages, files, etc.

import myPackage.security  # for abs import
from myPackage import security # also abs import
from ... import security # for relative import

import user  # abs import
from . import user  # for relative import


