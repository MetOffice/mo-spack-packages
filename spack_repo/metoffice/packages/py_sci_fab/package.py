# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

from spack.package import depends_on, variant, version
from spack_repo.builtin.build_systems.python import PythonPackage


class PySciFab(PythonPackage):
    """Fab - A Build System for Tomorrow!

    The Fab build system aims to provide a quick and easy build
    process tailored towards a specific subset of scientific software
    developers. Quick should be in both use and operation. Easy should
    mean the simple things are simple and the complicated things
    possible.
    """

    homepage = "https://github.com/MetOffice/fab"
    pypi = "sci-fab/sci_fab-0.10.1-py3-none-any.whl"

    version(
        "2.2.0",
        sha256="0e94538dfdc6bdcf0defabcc4eedaca59ea8b257239052b719c7e948e2bb58c2",
        expand=False,
    )

    version(
        "2.0.1",
        sha256="70430c2fb88272129866fa9c39e8e38a80a33abc6e8fa78e024c15360b801f54",
        expand=False,
    )

    version(
        "2.0.0",
        sha256="078566f16bb559e84f5148072931f91c4686049893cb149f3b46f8d66e00e81a",
        expand=False,
    )

    variant("clang", default=False, description="enable C support with clang")

    depends_on("python@3.10:")
    depends_on("py-fparser")
    depends_on("py-libclang", when="+clang")
