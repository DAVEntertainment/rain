"""
docgen entry
"""
from ci.docgen.docgen_builder import default_builder_config
from ci.docgen.docgen_builder import DocgenBuilder


def main():
    """
    doxygen build entry
    """
    config = default_builder_config()
    builder = DocgenBuilder()
    builder.setup(config)
    builder.run()


if "__main__" == __name__:
    main()
