from os.path import join as joinpath
from os.path import abspath, dirname
from sys import executable
from subprocess import Popen
from lint_utils import glob_files

ci_root = abspath(joinpath(dirname(__file__), '..', '..', 'ci'))
tests_root = abspath(joinpath(dirname(__file__), '..', '..', 'tests'))

py_files = glob_files(
    roots = (ci_root, tests_root),
    check_postfix = ('.py', ),
    skip_dirs = ()
)

cmd = f"{executable} -m pylint {' '.join(py_files)}"
print(cmd)

proc = Popen(cmd)
proc.communicate()
print(f"return code {proc.returncode}")
