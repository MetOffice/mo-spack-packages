# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import depends_on, version


class PyVernierTools(PythonPackage):
    """
    Python CLI and library for working with Vernier data
    """
    homepage = "https://github.com/MetOffice/Vernier"
    git = "https://github.com/MetOffice/Vernier.git"
    url = "https://github.com/MetOffice/Vernier/archive/refs/tags/0.4.0.tar.gz"

    version("develop", branch="main")

    depends_on("python@3.9:")
    depends_on("py-setuptools", type="build")

    build_directory = "post-processing"
