"""
CI entry
"""
import sys

from os.path import join as joinpath
from os.path import abspath, dirname

ci_main_root = abspath(dirname(__file__))
ci_root = abspath(joinpath(ci_main_root, '..'))
sys.path.insert(0, ci_root)

from ci.cpplint import cpplint
from ci.pylint import pylint
from ci.build import build
from ci.test import test
from ci.docgen import docgen


if '__main__' == __name__:
    cpplint.main()
    pylint.main()

    build.main()
    test.main()

    docgen.main()
