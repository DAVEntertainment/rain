"""
cpplint entry
"""
from os import walk
from os.path import join as joinpath
from os.path import sep as pathsep
from os.path import abspath, dirname
from sys import executable
from subprocess import Popen

#########################################################################
# utilities definitions
#########################################################################
def _filter_files_in_dir(root, files, check_postfix):
    """
    Filter files in given root
    signature:
        _filter_files_in_dir(root, files, check_postfix):
    params:
        root            root for files
        files           files before filter
        check_postfix   postfix to check
    """
    file_list = []
    for file in files:
        for postfix in check_postfix:
            if file.endswith(postfix):
                full_path = joinpath(root, file)
                file_list.append(full_path)
                break
    return file_list

def glob_files(roots, skip_dirs = (), check_postfix = ()):
    """
    Glob files
    signature:
        glob_files(roots, skip_dirs = (), check_postfix = ())
    params:
        roots           root list for globs
        skip_dirs       dir list to skip when glob
        check_postfix   postfix to check
    """
    file_list = []

    if len(check_postfix) == 0:
        return file_list

    for walk_root in roots:
        for root, _, files in walk(walk_root):
            path_coms = root.split(pathsep)
            for skip_dir in skip_dirs:
                if skip_dir in path_coms:
                    break
            else:
                file_list += _filter_files_in_dir(root, files, check_postfix)
    return file_list

#########################################################################
# start processing
#########################################################################
def main():
    """
    pylint entry
    signature:
        main()
    params:
    """
    src_root = abspath(joinpath(dirname(__file__), '..', '..', 'srcs'))
    tests_root = abspath(joinpath(dirname(__file__), '..', '..', 'tests'))

    submodules = [src_root, ]
    for module_root in (tests_root, ):
        for _, module_subs, _ in walk(module_root):
            for sub in module_subs:
                submodules.append(joinpath(module_root, sub))
            break

    for submodule in submodules:
        print(f"cpplint running for {submodule}")
        files = glob_files(
            roots = (submodule, ),
            check_postfix = ('.cpp', '.h', '.hpp', '.cc'),
            skip_dirs = ('.CMakeFiles', '.build', '.dist')
        )

        if len(files) == 0:
            continue

        cmd = f"{executable} -m cpplint {' '.join(files)}"
        print(cmd)

        with Popen(cmd) as proc:
            proc.communicate()
            print(f"return code {proc.returncode}")

if "__main__" == __name__:
    main()
