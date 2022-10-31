"""
file utils
"""
from os import walk, getcwd
from os.path import join as joinpath
from os.path import abspath
from os.path import sep as pathsep

def _filter_files_in_root(root, files, check_postfix, skip_files):
    """
    Filter files in given root

    signature:
        _filter_files_in_root(root, files, check_postfix, skip_files):

    params:
        root            root for files
        files           files before filter
        check_postfix   postfix to check
        skip_files      files to skip
    """
    file_list = []
    for file in files:
        for postfix in check_postfix:
            full_path = joinpath(root, file)
            if file in skip_files or full_path in skip_files:
                continue
            if file.endswith(postfix):
                file_list.append(full_path)
                break
    return file_list

def glob_files(roots, check_postfix = (), skip_dirs = (), skip_files = ()):
    """
    Glob files

    signature:
        glob_files(roots, skip_dirs = (), check_postfix = ())

    params:
        roots           root list to glob
        check_postfix   postfix to check
        skip_dirs       dir list to skip when glob
        skip_files      files to skip
    """
    file_list = []

    if len(check_postfix) == 0:
        return file_list

    for walk_root in roots:
        cur_skip_files = list(skip_files)
        for index, _ in enumerate(cur_skip_files):
            if abspath(cur_skip_files[index]) != abspath(joinpath(getcwd(), cur_skip_files[index])):
                cur_skip_files[index] = abspath(joinpath(walk_root, cur_skip_files[index]))
        for root, _, files in walk(walk_root):
            path_coms = root.split(pathsep)
            for skip_dir in skip_dirs:
                if skip_dir in path_coms:
                    break
            else:
                file_list += _filter_files_in_root(root, files, check_postfix, cur_skip_files)
    return file_list
