"""
CI entry
"""
from rain.shell_utils import run_cmd
from sys import executable
from os.path import exists as existspath
from os.path import join as joinpath
from os.path import abspath, dirname

class CIFailed(Exception):
    """
    CI failure error
    """


if '__main__' == __name__:
    ci_root = abspath(dirname(__file__))
    ret = run_cmd(f"{executable} {joinpath(ci_root, 'cpplint', 'cpplint.py')}")
    if ret != 0:
        raise CIFailed(f"cpplint failed")
    ret = run_cmd(f"{executable} {joinpath(ci_root, 'pylint', 'pylint.py')}")
    if ret != 0:
        raise CIFailed(f"pylint failed")

    ret = run_cmd(f"{executable} {joinpath(ci_root, 'build', 'build.py')}")
    if ret != 0:
        raise CIFailed(f"build failed")
    ret = run_cmd(f"{executable} {joinpath(ci_root, 'test', 'test.py')}")
    if ret != 0:
        raise CIFailed(f"test failed")

    ret = run_cmd(f"{executable} {joinpath(ci_root, 'docgen', 'docgen.py')}")
    if ret != 0:
        raise CIFailed(f"docgen failed")

