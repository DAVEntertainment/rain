from os import walk
from os.path import join as joinpath
from os.path import sep as pathsep

def glob_files(roots, skip_dirs = (), check_postfix = ()):
    file_list = []

    if len(check_postfix) == 0:
        return file_list

    for walk_root in roots:
        for r, ds, fs in walk(walk_root):
            path_coms = r.split(pathsep)
            for s in skip_dirs:
                if s in r:
                    break
            else:
                for f in fs:
                    for postfix in check_postfix:
                        if f.endswith(postfix):
                            full_path = joinpath(r, f)
                            file_list.append(full_path)
                            break
    return file_list
