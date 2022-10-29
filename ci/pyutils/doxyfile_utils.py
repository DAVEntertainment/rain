"""
doxyfile utils
"""
import re
from os.path import join as joinpath
from os.path import abspath, dirname

def search_var(content, var_name):
    """
    Search variable string in doxyfile

    """
    matched = re.findall(
        r"(^\s*(" + var_name + r"\s*)=(\s*(\".*\"|[\w\-\.\*\+]+)\s*\\?$)*)",
        content,
        re.MULTILINE
    )
    print(matched)

    if len(matched) == 0:
        print(f"doxyfile option {var_name} not found")
        return None, None, None

    if len(matched) > 1:
        print(f"doxyfile option {var_name} multiple found:")
        for match in matched:
            print(f"  {match[0].strip()}")
        return None, None, None

    full_str, var_name_prefix, _, value_str = matched[0]
    return full_str.strip(), var_name_prefix, value_str


def replace_vars(content, **kwargs):
    """
    Replace variable string with given value in doxyfile
    """
    for key, value in kwargs.items():
        full_str, prefix, _ = search_var(content, key)
        if isinstance(value, list):
            value_str_gen = ''
            indent = ("{:" + str(len(prefix) + 2) + "}").format(" ")
            for index, item in enumerate(value):
                value_str_gen += ("" if index == 0 else indent) + "{}{}".format(
                    item,
                    "" if index == len(value)-1 else " \\\n"
                )
            full_str_gen = f"{prefix}= {value_str_gen}"
        else:
            full_str_gen = f"{prefix}= {value}"
        content = content.replace(full_str, full_str_gen)
    return content

#####################################################################################
# Examples
#####################################################################################
def __example_search_var_in_doxyfile():
    """
    Example for search_var
    """
    srcs_root = abspath(joinpath(dirname(__file__), '..', '..', 'srcs'))
    doxyfile_in = joinpath(srcs_root, 'doxyfile.in')

    with open(doxyfile_in, mode = 'r', encoding = 'utf-8') as stream:
        doxyfile_content = stream.read()

    search_var(doxyfile_content, "QUIET")
    search_var(doxyfile_content, "WARN_FORMAT")
    search_var(doxyfile_content, "INPUT")
    search_var(doxyfile_content, "INPUT_ENCODING")
    search_var(doxyfile_content, "FILE_PATTERNS")


def __example_gen_doxyfile():
    """
    Example for replace_vars
    """
    srcs_root = abspath(joinpath(dirname(__file__), '..', '..', 'srcs'))
    doxyfile_in = joinpath(srcs_root, 'doxyfile.in')
    doxyfile_out = joinpath(srcs_root, 'doxyfile')

    with open(doxyfile_in, mode = 'r', encoding = 'utf-8') as stream:
        doxyfile_content = stream.read()

    doxyfile_content = replace_vars(
        doxyfile_content,
        INPUT = ["rain.h","rain.cpp"],
        INPUT_ENCODING = "GBK"
    )

    with open(doxyfile_out, mode = 'w', encoding = 'utf-8') as stream:
        stream.write(doxyfile_content)

#####################################################################################
# Entry for examples
#####################################################################################
if "__main__" == __name__:
    # __example_search_var_in_doxyfile()
    # __example_gen_doxyfile()
    pass
