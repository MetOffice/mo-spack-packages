# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyFortitude(PythonPackage):
    """A Fortran Linter. Fortitude is built on Ruff, written in Rust and installable with Python."""

    homepage = "https://github.com/PlasmaFAIR/fortitude"
    pypi = "fortitude-lint/fortitude_lint-0.7.3.tar.gz"
    license("MIT")

    version("0.7.3", sha256="bbc631ca5882f83819c223c3707a8a0cca2a3821aa4ab0be6504974557224a59")
    version("0.7.4", sha256="be6407f4051d1db0134c3beeeb0bb71d3f9b9aceb953759c61c82b4689b6cd9e")
    version("0.7.5", sha256="5a0c6d38a6444fbe31d1724c14672181a264e48d755629b757e9b10c688685d9")


    depends_on("py-maturin@1.0:2.0", type=("build"))
    depends_on("python@3.10:")
