"""
Base builder classes
"""

class Step:
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


class Builder:
    """
    Base builder
        a builder to control build procedure
    """

    def __init__(self):
        """
        init builder
        """
        self.config = None
        self.parser = None
        self.steps = []

        self._setup_steps()

    def _setup_steps(self):
        """
        setup builder's build steps
        """
        # self.steps.append(StepBase())

    def _setup_dependencies(self):
        """
        setup builder's steps' dependencies
        """

    def setup(self, config):
        """
        setup builder
        """
        self.config = config
        self._setup_dependencies()

    def run(self):
        """
        run builder
        """
        for step in self.steps:
            step.setup(self.config)
            step.run()
