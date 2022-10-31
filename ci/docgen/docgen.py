"""
docgen entry
"""
from ci.docgen.docgen_builder import DocgenBuilder, DocgenBuilderConfig


def main():
    """
    doxygen build entry
    """
    config = DocgenBuilderConfig()
    builder = DocgenBuilder()
    builder.setup(config)
    builder.run()


if "__main__" == __name__:
    main()
