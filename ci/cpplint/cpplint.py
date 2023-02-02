"""
cpplint entry
"""
import sys
from os.path import join as joinpath
from os.path import abspath, dirname
from types import SimpleNamespace
from rain.path_utils import glob_files
from rain.lint_utils import split_modules
from rain.shell_utils import run_cmd


class LintFailed(Exception):
    """
    lint failed
    """


def run_lint(config):
    """
    run cpplint
    """
    statistics = {}
    for module in config.modules:
        print(f"cpplint running for {module}")
        module_stats = statistics[module] = {}

        files = glob_files(
            roots = (module, ),
            check_postfix = config.post_fix,
            skip_dirs = config.skip_dirs
        )

        module_stats['files'] = len(files)
        if len(files) > 0:
            module_stats['code'] = run_cmd(f"{sys.executable} -m cpplint {' '.join(files)}")
        else:
            print(r"no files found for cpplint")
            module_stats['code'] = 0
    return statistics

def analyze_summary(statistics):
    """
    analyze cpplint summary
    """
    summary = SimpleNamespace()
    summary.summary = SimpleNamespace()
    summary.modules = statistics

    for module, module_stats in statistics.items():
        module_stats['success'] = module_stats['code'] == 0

    summary.summary.modules = len(statistics)
    summary.summary.success = sum((
        module_stats['code'] == 0 for module, module_stats in statistics.items()
    ))

    return summary

def print_summary(summary):
    """
    print summary
    """
    print(r"cpplint summary:")
    print(f"  modules: {summary.summary.modules}")
    print(f"  success: {summary.summary.success}")
    for module, module_stas in summary.modules.items():
        print(f"  module {module}")
        print(f"    code   : {module_stas['code']}")
        print(f"    success: {module_stas['success']}")
        print(f"    files  : {module_stas['files']}")

def main():
    """
    cpplint entry
    """
    print("start from rain cpplint entry")

    config = SimpleNamespace()
    config.repo_root = abspath(joinpath(dirname(__file__), '..', '..'))
    config.include_root = joinpath(config.repo_root, 'include')
    config.src_root = joinpath(config.repo_root, 'src')
    config.tests_root = joinpath(config.repo_root, 'tests')

    config.modules = [config.src_root, config.include_root] + split_modules((config.tests_root, ))
    config.post_fix = ('.cpp', '.h', '.hpp', '.cc')
    config.skip_dirs = ('.CMakeFiles', '.build', '.dist')
    config.skip_files = ('rain_api.h', )

    statistics = run_lint(config)
    summary = analyze_summary(statistics)
    print_summary(summary)

    if summary.summary.modules != summary.summary.success:
        raise LintFailed()


if "__main__" == __name__:
    main()
