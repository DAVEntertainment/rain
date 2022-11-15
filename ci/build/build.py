"""
build entry
"""
from os import cpu_count
from os.path import join as joinpath
from os.path import exists as existspath
from os.path import abspath, dirname
from shutil import rmtree
from types import SimpleNamespace
from ci.pyutils.builder import Step, Builder
from ci.pyutils.shell_utils import run_cmd



class BuildFailed(Exception):
    """
    build failed
    """


class StepClean(Step):
    """
    step clean
    """

    def __rmdir(self, directory):
        if existspath(directory):
            print(f"removing {directory}")
            rmtree(directory)

    def run(self):
        if not self.config.clean:
            print("skipping step clean")
            return

        print("running step clean")
        if existspath(self.config.build_dir):
            run_cmd(
                f"cmake --build {self.config.build_dir} --target clean"
            )
        self.__rmdir(self.config.build_dir)
        self.__rmdir(joinpath(self.config.repo_root, 'bin'))
        self.__rmdir(joinpath(self.config.repo_root, 'include'))
        self.__rmdir(joinpath(self.config.repo_root, 'lib'))


class StepConfigure(Step):
    """
    step build
    """

    def run(self):
        if not self.config.configure:
            print("skipping step configure")
            return

        print("running step configure")
        ret = run_cmd(
            f"cmake -G\"{self.config.generator}\""
            + f" -A {self.config.architecture}"
            + f" -S {self.config.repo_root}"
            + f" -B {self.config.build_dir}"
            + f" -DCMAKE_INSTALL_PREFIX={self.config.repo_root}"
            + f" -DCMAKE_DEBUG_POSTFIX={self.config.debug_postfix}"
        )
        if 0 != ret:
            raise BuildFailed(f"cmake configure failed with code {ret}")


class StepBuild(Step):
    """
    step build
    """

    def run(self):
        if not self.config.build:
            print("skipping step build")
            return

        print("running step build")
        ret = run_cmd(
            f"cmake --build {self.config.build_dir}"
            + f" --config {'Debug' if self.config.debug else 'Release'}"
            + f" -j{cpu_count()+1}"
        )
        if 0 != ret:
            raise BuildFailed(f"build failed with code {ret}")


class StepPack(Step):
    """
    step pack
    """

    def run(self):
        if not self.config.pack:
            print("skipping step pack")
            return

        print("running step pack")
        ret = run_cmd(
            f"cmake --install {self.config.build_dir}"
            + f" --config {'Debug' if self.config.debug else 'Release'}"
        )
        if 0 != ret:
            raise BuildFailed(f"install failed with code {ret}")


class RainBuilder(Builder):
    """
    Doxygen builder
    """

    def _setup_steps(self):
        self.steps.append(StepClean())
        self.steps.append(StepConfigure())
        self.steps.append(StepBuild())
        self.steps.append(StepPack())

    def _setup_dependencies(self):
        pass


def default_builder_config():
    """
    default builder config
    """
    config = SimpleNamespace()

    # procedure control
    config.clean = True
    config.configure = True
    config.build = True
    config.pack = True

    # build config
    config.build_root = abspath(dirname(__file__))
    config.repo_root = abspath(joinpath(config.build_root, '..', '..'))
    config.build_dir = abspath(joinpath(config.build_root, '.build'))
    config.install_dir = abspath(config.repo_root)
    config.generator = "Visual Studio 16 2019"
    config.architecture = "x64"
    config.debug = False
    config.debug_postfix = "d"

    return config


def main():
    """
    build entry
    """
    print("start from rain build entry")
    config = default_builder_config()
    builder = RainBuilder()
    # build release
    config.clean = False
    config.debug = False
    builder.setup(config)
    builder.run()
    # build debug
    config.clean = False
    config.debug = True
    builder.setup(config)
    builder.run()


if "__main__" == __name__:
    main()
