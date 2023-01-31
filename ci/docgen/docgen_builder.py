"""
docgen builder
"""
import sys
import json
from os.path import join as joinpath
from os.path import exists as existspath
from os.path import abspath, dirname
from os import makedirs
from shutil import rmtree
from types import SimpleNamespace
from ci.pyutils.builder import Step, Builder
from ci.pyutils import doxyfile_utils
from ci.pyutils.path_utils import glob_files
from ci.pyutils.shell_utils import run_cmd


class BuildFailed(Exception):
    """
    build failed
    """

class StepClean(Step):
    """
    step clean
    """

    def run(self):
        if not self.config.clean:
            print("skipping step clean")
            return

        print("running step clean")
        if existspath(self.config.build_dir):
            rmtree(self.config.build_dir)


class StepRunDoxygen(Step):
    """
    step run doxygen
    """

    def __search_sources_input(self):
        sources = []
        sources.append(joinpath(self.config.repo_root, "README.md"))
        sources.extend(glob_files(
            roots = (self.config.srcs_root, self.config.include_root),
            check_postfix = ('.cpp', '.h', '.hpp', '.cc', 'CMakeLists.txt', 'README.md'),
            skip_dirs = ('.CMakeFiles', '.build', '.dist')
        ))
        return sources

    def __prepare_doxyfile_input(self):
        doxyfile_input = {
            "OUTPUT_DIRECTORY": self.config.doxygen_out,
            "INPUT": self.__search_sources_input(),
            "GENERATE_XML": "YES",
            "XML_OUTPUT": self.config.doxygen_xml_out
        }
        return doxyfile_input

    def __generate_doxyfile(self):
        doxyfile_input = self.__prepare_doxyfile_input()
        with open(self.config.doxyfile_in, mode = 'r', encoding = 'utf-8') as stream:
            content = stream.read()
        content = doxyfile_utils.replace_vars(content, **doxyfile_input)
        with open(self.config.doxyfile_out, mode = 'w', encoding = 'utf-8') as stream:
            stream.write(content)

    def __run_doxygen(self):
        if not existspath(self.config.doxygen_out):
            makedirs(self.config.doxygen_out)

        cmd = f"doxygen {self.config.doxyfile_out}"
        code = run_cmd(cmd)
        if code != 0:
            raise BuildFailed(f"run doxygen failed with code {code}")

    def run(self):
        if not self.config.run_doxygen:
            print("skipping step doxygen")
            return

        print("running step doxygen")
        self.__generate_doxyfile()
        self.__run_doxygen()


class StepRunSphinx(Step):
    """
    step run sphinx
    """

    def __gen_shpinx_config_file(self):
        sphinx_config = {}

        if existspath(self.config.sphinx_config_file):
            with open(self.config.sphinx_config_file, mode = 'r', encoding = 'utf-8') as stream:
                config = json.load(stream)
            sphinx_config.update(config)

        sphinx_config['breathe_projects'] = {
            'rain': joinpath(self.config.doxygen_out, self.config.doxygen_xml_out)
        }
        sphinx_config['search_paths'] = [
            self.config.repo_root
        ]

        with open(self.config.sphinx_config_file, mode = 'w', encoding = 'utf-8') as stream:
            json.dump(sphinx_config, stream, indent = 2)


    def __run_shpinx(self):
        cmd = f"{sys.executable} -m sphinx.cmd.build " \
            + f"-b html {self.config.docgen_root} {self.config.sphinx_out}"
        code = run_cmd(cmd)
        if code != 0:
            raise BuildFailed(f"run sphinx failed with code {code}")

    def run(self):
        if not self.config.run_sphinx:
            print("skipping step sphinx")
            return

        print("running step sphinx")
        self.__gen_shpinx_config_file()
        self.__run_shpinx()


class DocgenBuilder(Builder):
    """
    Doxygen builder
    """

    def _setup_steps(self):
        self.steps.append(StepClean())
        self.steps.append(StepRunDoxygen())
        self.steps.append(StepRunSphinx())

    def _setup_dependencies(self):
        pass


def default_builder_config():
    """
    default builder config
    """
    config = SimpleNamespace()

    # procedure control
    config.clean = False
    config.run_doxygen = True
    config.run_sphinx = True

    # build config
    config.docgen_root = abspath(dirname(__file__))
    config.repo_root = abspath(joinpath(config.docgen_root, '..', '..'))
    config.include_root = abspath(joinpath(config.repo_root, 'include'))
    config.srcs_root = abspath(joinpath(config.repo_root, 'src'))
    config.build_dir = joinpath(config.docgen_root, '.build')
    #   doxygen config
    config.doxyfile_in = joinpath(config.docgen_root, 'doxyfile.in')
    config.doxyfile_out = joinpath(config.docgen_root, 'doxyfile')
    config.doxygen_out = joinpath(config.build_dir, 'doxygen')
    config.doxygen_xml_out = 'xml'
    #   sphinx config
    config.sphinx_config_file = joinpath(config.docgen_root, 'sphinx-config.json')
    config.sphinx_out = joinpath(config.build_dir, 'sphinx')

    return config
