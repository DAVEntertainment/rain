"""
pylint entry
"""
import sys
from os.path import join as joinpath
from os.path import abspath, dirname
from ci.pyutils.path_utils import glob_files
from ci.pyutils.lint_utils import split_modules
from ci.pyutils.shell_utils import run_cmd


class BuildFailed(Exception):
    """
    build failed
    """


def main():
    """
    pylint entry

    signature:
        main()

    params:
    """
    ci_root = abspath(joinpath(dirname(__file__), '..', '..', 'ci'))
    docgen_root = abspath(joinpath(dirname(__file__), '..', '..', 'ci', 'docgen'))
    tests_root = abspath(joinpath(dirname(__file__), '..', '..', 'tests'))

    modules = [ci_root, ] + split_modules((tests_root, ))

    for module in modules:
        print(f"pylint running for {module}")
        files = glob_files(
            roots = (module, ),
            check_postfix = ('.py', ),
            skip_dirs = (),
            skip_files = (joinpath(docgen_root, 'conf.py'), )
        )

        if len(files) == 0:
            continue

        code = run_cmd(f"{sys.executable} -m pylint {' '.join(files)}")
        if code != 0:
            raise BuildFailed(f"run pylint failed with code {code}")

if "__main__" == __name__:
    main()
