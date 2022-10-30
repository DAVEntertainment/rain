"""
cpplint entry
"""
import sys
from os.path import join as joinpath
from os.path import abspath, dirname
from ci.pyutils.path_utils import glob_files
from ci.pyutils.lint_utils import split_modules
from ci.pyutils.shell_utils import run_cmd

def main():
    """
    pylint entry

    signature:
        main()

    params:
    """
    src_root = abspath(joinpath(dirname(__file__), '..', '..', 'srcs'))
    tests_root = abspath(joinpath(dirname(__file__), '..', '..', 'tests'))

    modules = [src_root, ] + split_modules((tests_root, ))

    for module in modules:
        print(f"cpplint running for {module}")
        files = glob_files(
            roots = (module, ),
            check_postfix = ('.cpp', '.h', '.hpp', '.cc'),
            skip_dirs = ('.CMakeFiles', '.build', '.dist')
        )

        if len(files) == 0:
            continue

        run_cmd(f"{sys.executable} -m cpplint {' '.join(files)}")

if "__main__" == __name__:
    main()
