"""
docgen entry
"""
from os.path import join as joinpath
from os.path import abspath, dirname
from ci.pyutils import doxyfile_utils

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

    doxyfile_utils.search_var(doxyfile_content, "QUIET")
    doxyfile_utils.search_var(doxyfile_content, "WARN_FORMAT")
    doxyfile_utils.search_var(doxyfile_content, "INPUT")
    doxyfile_utils.search_var(doxyfile_content, "INPUT_ENCODING")
    doxyfile_utils.search_var(doxyfile_content, "FILE_PATTERNS")

def __example_gen_doxyfile():
    """
    Example for doxyfile_utils.replace_vars
    """
    srcs_root = abspath(joinpath(dirname(__file__), '..', '..', 'srcs'))
    doxyfile_in = joinpath(srcs_root, 'doxyfile.in')
    doxyfile_out = joinpath(srcs_root, 'doxyfile')

    with open(doxyfile_in, mode = 'r', encoding = 'utf-8') as stream:
        doxyfile_content = stream.read()

    doxyfile_content = doxyfile_utils.replace_vars(
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
