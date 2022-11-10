"""
CI entry
"""
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
