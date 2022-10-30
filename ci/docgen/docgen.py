"""
docgen entry
"""
import sys
from os.path import join as joinpath
from os.path import exists as existspath
from os.path import abspath, dirname
from os import makedirs
from types import SimpleNamespace
from ci.pyutils.builder import Step, Builder
from ci.pyutils import doxyfile_utils
from ci.pyutils.path_utils import glob_files
from ci.pyutils.shell_utils import run_cmd



class SetupGenDoxyfile(Step):
    """
    step generate doxyfile form doxyfile.in
    """

    def __search_sources_input(self):
        """
        search source files
        """
        sources = []
        sources.append(joinpath(self.config.repo_root, "README.md"))
        sources.extend(glob_files(
            roots = (self.config.srcs_root, ),
            check_postfix = ('.cpp', '.h', '.hpp', '.cc', 'CMakeLists.txt', 'README.md'),
            skip_dirs = ('.CMakeFiles', '.build', '.dist')
        ))
        return sources

    def __prepare_doxyfile_input(self):
        """
        prepare doxyfile input
        """
        doxyfile_input = {
            "OUTPUT_DIRECTORY": self.config.doxygen_out,
            "INPUT": self.__search_sources_input()
        }
        return doxyfile_input

    def run(self):
        """
        run step
        """
        doxyfile_input = self.__prepare_doxyfile_input()
        with open(self.config.doxyfile_in, mode = 'r', encoding = self.config.doxyfile_encoding) as stream:
            content = stream.read()
        content = doxyfile_utils.replace_vars(content, **doxyfile_input)
        with open(self.config.doxyfile_out, mode = 'w', encoding = self.config.doxyfile_encoding) as stream:
            stream.write(content)


class SetupRunDoxygen(Step):
    """
    step run doxygen
    """

    def run(self):
        """
        run step
        """

        if not existspath(self.config.doxygen_out):
            makedirs(self.config.doxygen_out)

        cmd = f"doxygen {self.config.doxyfile_out}"
        run_cmd(cmd)


class SetupRunSphinx(Step):
    """
    step run sphinx
    """

    def run(self):
        """
        run step
        """

        cmd = f"{sys.executable} -m sphinx.cmd.build -b html {self.config.docgen_root} {self.config.sphinx_out}"
        run_cmd(cmd)


class DoxygenBuilder(Builder):
    """
    Doxygen builder
    """

    def _setup_steps(self):
        self.steps.append(SetupGenDoxyfile())
        self.steps.append(SetupRunDoxygen())
        self.steps.append(SetupRunSphinx())


def main():
    """
    doxygen build entry
    """
    config = SimpleNamespace()

    config.docgen_root = abspath(dirname(__file__))
    config.repo_root = abspath(joinpath(config.docgen_root, '..', '..'))
    config.srcs_root = abspath(joinpath(config.repo_root, 'srcs'))
    config.doxyfile_encoding = 'utf-8'
    config.doxyfile_in = joinpath(config.docgen_root, 'doxyfile.in')
    config.doxyfile_out = joinpath(config.docgen_root, 'doxyfile')
    config.doxygen_out = joinpath(config.docgen_root, '.build', 'doxygen')
    config.sphinx_out = joinpath(config.docgen_root, '.build', 'sphinx')

    builder = DoxygenBuilder()
    builder.setup(config)
    builder.run()


if "__main__" == __name__:
    main()
