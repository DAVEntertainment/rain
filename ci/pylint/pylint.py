"""
pylint entry
"""
import sys
from os.path import join as joinpath
from os.path import abspath, dirname
from types import SimpleNamespace
from ci.pyutils.path_utils import glob_files
from ci.pyutils.lint_utils import split_modules
from ci.pyutils.shell_utils import run_cmd


class LintFailed(Exception):
    """
    lint failed
    """


def run_lint(config):
    """
    run pylint
    """
    statistics = {}
    for module in config.modules:
        print(f"pylint running for {module}")
        module_stats = statistics[module] = {}

        files = glob_files(
            roots = (module, ),
            check_postfix = config.post_fix,
            skip_dirs = config.skip_dirs,
            skip_files = config.skip_files
        )

        module_stats['files'] = len(files)
        if len(files) > 0:
            module_stats['code'] = run_cmd(f"{sys.executable} -m pylint {' '.join(files)}")
        else:
            print(r"no files found for pylint")
            module_stats['code'] = 0
    return statistics

def analyze_summary(statistics):
    """
    analyze pylint summary
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
    print(r"pylint summary:")
    print(r"  summary:")
    print(f"    modules: {summary.summary.modules}")
    print(f"    success: {summary.summary.success}")
    for module, module_stas in summary.modules.items():
        print(f"  module {module}")
        print(f"    code   : {module_stas['code']}")
        print(f"    success: {module_stas['success']}")
        print(f"    files  : {module_stas['files']}")

def main():
    """
    pylint entry
    """
    print("start from rain pylint entry")

    config = SimpleNamespace()
    config.repo_root = abspath(joinpath(dirname(__file__), '..', '..'))
    config.ci_root = joinpath(config.repo_root, 'ci')
    config.docgen_root = joinpath(config.repo_root, 'ci', 'docgen')
    config.tests_root = joinpath(config.repo_root, 'tests')

    config.modules = split_modules((config.ci_root, config.tests_root))
    config.post_fix = ('.py', )
    config.skip_dirs = ('__pycache__', )
    config.skip_files = (joinpath(config.docgen_root, 'conf.py'), )

    statistics = run_lint(config)
    summary = analyze_summary(statistics)
    print_summary(summary)

    if summary.summary.modules != summary.summary.success:
        raise LintFailed()


if "__main__" == __name__:
    main()
