# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

from spack_repo.builtin.packages.py_psyclone.package import PyPsyclone as PyPsycloneBase
from spack.package import version, depends_on


class PyPsyclone(PyPsycloneBase):
    """
    A source-to-source Fortran compiler designed to programmatically optimise,
    parallelise and instrument HPC applications (written in Fortran) via user-
    provided transformation scripts. Additionally, PSyclone supports the
    development of kernel-based, Fortran-embedded DSLs and is used in the UK
    Met Office's next-generation modelling system, LFRic.
    """

    version(
        "3.3.1",
        sha256="9d256cc4ee1494286b1ed8b4b8447b576748008ea5e236159717db1ddc3bd09a",
    )

    version(
        "3.3.0",
        sha256="9a8c6dc425ef666b9340641fad64e6496302c746a12b23cabd887a1885831c85",
    )

    version(
        "3.2.2",
        sha256="8452fad84a2e61566e8599dc6ff336c4ada73ec03e17900aa5d37afe656d46d5",
    )

    depends_on("py-fparser@0.2.4:", type=("build", "run"), when="@3.3.0:")

    # Adjoint fails with sympy >= 1.14
    depends_on("py-sympy@=1.13.3", type=("build", "run"), when="@3.3.0:3.3.1")
