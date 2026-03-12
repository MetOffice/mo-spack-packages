# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


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
