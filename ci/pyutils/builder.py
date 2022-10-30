"""
Base builder classes
"""

class StepBase:
    """
    Base build step
        a build step in a builder
    """

    def __init__(self):
        """
        init build step
        """
        self.config = None

    def setup(self, config):
        """
        setup build step
        """
        self.config = config

    def run(self):
        """
        run build step
        """


class BuilderBase:
    """
    Base builder
    """

    def __init__(self):
        """
        init builder
        """
        self.arguments = None
        self.config = None
        self.parser = None
        self.steps = []

        self._setup_argument_parser()
        self._setup_steps()

    def _setup_argument_parser(self):
        """
        setup argument parser for builder
        """
        # from argparse import ArgumentParser
        # self.parser = ArgumentParser()

    def _setup_steps(self):
        """
        setup builder's build steps
        """
        # self.steps.append(StepBase())

    def _setup_dependencies(self):
        """
        setup builder's steps' dependencies
        """

    def setup(self, arguments):
        """
        setup builder
        """
        self.arguments = arguments
        self.config = self.parser.parse_args(
            args = arguments
        )
        self._setup_dependencies()

    def run(self):
        """
        run builder
        """
        for step in self.steps:
            step.setup(self.config)
            step.run()
