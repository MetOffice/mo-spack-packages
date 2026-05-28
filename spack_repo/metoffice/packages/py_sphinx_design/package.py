# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------
from spack_repo.builtin.packages.py_sphinx_design.package import PySphinxDesign as PySphinxDesignBase

from spack.package import version, depends_on


class PySphinxDesign(PySphinxDesignBase):
    """A sphinx extension for designing beautiful, screen-size responsive web components."""

    version("0.7.0", sha256="d2a3f5b19c24b916adb52f97c5f00efab4009ca337812001109084a740ec9b7a")

    depends_on("py-sphinx@7:10", when="@0.7.0:", type=("build", "run"))
