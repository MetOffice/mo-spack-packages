# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

from spack.package import depends_on, version
from spack_repo.builtin.build_systems.python import PythonPackage


class PyRosePicker(PythonPackage):
    """py-rose-picker - metadata utility for LFRIC."""

    homepage = "https://github.com/MetOffice/rose_picker"
    url = "https://github.com/MetOffice/rose_picker/archive/refs/tags/2026.03.2.tar.gz"
    git = "https://github.com/MetOffice/rose_picker.git"

    version("develop", branch="main")
    version(
        "2026.03.2",
        sha256="9d35cde4edee0069635b8170dd9e017f86f6a8f85b34917fbab545616edd1ce2",
    )

    depends_on("python@3:")
    depends_on("py-setuptools", type="build")
