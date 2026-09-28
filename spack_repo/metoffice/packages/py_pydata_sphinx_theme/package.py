# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

import spack_repo.builtin.packages.py_pydata_sphinx_theme.package as pyPydataSphinxTheme
from spack.package import version


class PyPydataSphinxTheme(pyPydataSphinxTheme.PyPydataSphinxTheme):
    """A clean, three-column, Bootstrap-based Sphinx theme by and for the PyData community."""

    version(
        "0.17.1",
        sha256="2cfc1d926c753c77039b7ee53f0ccebcbee5e81f0db61432b01cbb10ad7fd0af",
    )
    version(
        "0.17.0",
        sha256="529c5631582cb3328cf4814fb9eb80611d1704c854406d282a75c9c86e3a1955",
    )
