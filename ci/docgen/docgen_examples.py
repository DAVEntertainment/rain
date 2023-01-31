"""
docgen examples
"""
from os.path import join as joinpath
from os.path import abspath, dirname
from rain import doxyfile_utils

#####################################################################################
# Examples
#####################################################################################
def example_search_var_in_doxyfile():
    """
    Example for search_var
    """
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("running example_search_var_in_doxyfile ...")
    docgen_root = abspath(dirname(__file__))
    doxyfile_in = joinpath(docgen_root, 'doxyfile.in')

    with open(doxyfile_in, mode = 'r', encoding = 'utf-8') as stream:
        doxyfile_content = stream.read()

    doxyfile_utils.search_var(doxyfile_content, "QUIET")
    doxyfile_utils.search_var(doxyfile_content, "WARN_FORMAT")
    doxyfile_utils.search_var(doxyfile_content, "INPUT")
    doxyfile_utils.search_var(doxyfile_content, "INPUT_ENCODING")
    doxyfile_utils.search_var(doxyfile_content, "FILE_PATTERNS")

def example_gen_doxyfile():
    """
    Example for doxyfile_utils.replace_vars
    """
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("running example_gen_doxyfile ...")
    docgen_root = abspath(dirname(__file__))
    doxyfile_in = joinpath(docgen_root, 'doxyfile.in')
    doxyfile_out = joinpath(docgen_root, 'doxyfile')

    with open(doxyfile_in, mode = 'r', encoding = 'utf-8') as stream:
        doxyfile_content = stream.read()

    doxyfile_content = doxyfile_utils.replace_vars(
        doxyfile_content,
        INPUT = ["rain.h", "rain.cpp"],
        INPUT_ENCODING = "GBK"
    )

    with open(doxyfile_out, mode = 'w', encoding = 'utf-8') as stream:
        stream.write(doxyfile_content)

#####################################################################################
# Entry for examples
#####################################################################################
if "__main__" == __name__:
    # example_search_var_in_doxyfile()
    # example_gen_doxyfile()
    pass
