# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

from spack_repo.builtin.packages.py_psyclone.package import PyPsyclone as PyPsycloneBase
from spack.package import version


class PyPsyclone(PyPsycloneBase):
    """
    A source-to-source Fortran compiler designed to programmatically optimise,
    parallelise and instrument HPC applications (written in Fortran) via user-
    provided transformation scripts. Additionally, PSyclone supports the
    development of kernel-based, Fortran-embedded DSLs and is used in the UK
    Met Office's next-generation modelling system, LFRic.
    """

    version(
        "3.3.0-rc1",
        sha256="f9e6deece4e874c22235bfac0e80c7b7afedf6864a515f276a69bda5ca1d0e7c",
    )
    version(
        "3.2.2",
        sha256="8452fad84a2e61566e8599dc6ff336c4ada73ec03e17900aa5d37afe656d46d5",
    )

