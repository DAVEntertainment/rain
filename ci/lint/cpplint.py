from os.path import join as joinpath
from os.path import abspath, dirname
from sys import executable
from subprocess import Popen
from lint_utils import glob_files

src_root = abspath(joinpath(dirname(__file__), '..', '..', 'srcs'))
tests_root = abspath(joinpath(dirname(__file__), '..', '..', 'tests'))

cpp_files = glob_files(
    roots = (src_root, tests_root),
    check_postfix = ('.cpp', '.h', '.hpp', '.cc'),
    skip_dirs = ('.CMakeFiles', '.build', '.dist')
)

cmd = f"{executable} -m cpplint {' '.join(cpp_files)}"
print(cmd)

proc = Popen(cmd)
proc.communicate()
print(f"return code {proc.returncode}")
