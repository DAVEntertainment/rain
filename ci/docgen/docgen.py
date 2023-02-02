"""
docgen entry
"""
from docgen_builder import default_builder_config
from docgen_builder import DocgenBuilder


def main():
    """
    docgen build entry
    """
    print("start from rain docgen build entry")
    config = default_builder_config()
    builder = DocgenBuilder()
    builder.setup(config)
    builder.run()


if "__main__" == __name__:
    main()
