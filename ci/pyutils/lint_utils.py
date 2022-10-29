"""
lint utils
"""
from os import walk
from os.path import join as joinpath
from os.path import sep as pathsep

def _filter_files_in_root(root, files, check_postfix):
    """
    Filter files in given root

    signature:
        _filter_files_in_root(root, files, check_postfix):

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
        roots           root list to glob
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
                file_list += _filter_files_in_root(root, files, check_postfix)
    return file_list

def split_modules(roots):
    """
    Split modules into submodules

    signature:
        split_modules(roots)

    params:
        roots           root list to search
    """
    submodules = []
    for module_root in roots:
        for _, module_subs, _ in walk(module_root):
            for sub in module_subs:
                submodules.append(joinpath(module_root, sub))
            break
    return submodules
