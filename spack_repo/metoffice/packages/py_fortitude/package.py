# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import depends_on, license, version


class PyFortitude(PythonPackage):
    """A Fortran Linter. Fortitude is built on Ruff, written in Rust and installable with Python."""

    homepage = "https://github.com/PlasmaFAIR/fortitude"
    pypi = "fortitude-lint/fortitude_lint-0.7.3.tar.gz"
    license("MIT")

    version(
        "0.9.0", 
        sha256="7d51706a0a15bdc3ad6521214062c17e921dd1093759d15d785da4a59950d39d"
    )
    version(
        "0.8.0",
        sha256="01662917f0b87792fcb5d8c4b1e893849d79d1b92dade7cc836c0e145b651188",
    )
    version(
        "0.7.5",
        sha256="5a0c6d38a6444fbe31d1724c14672181a264e48d755629b757e9b10c688685d9",
    )
    version(
        "0.7.4",
        sha256="be6407f4051d1db0134c3beeeb0bb71d3f9b9aceb953759c61c82b4689b6cd9e",
    )
    version(
        "0.7.3",
        sha256="bbc631ca5882f83819c223c3707a8a0cca2a3821aa4ab0be6504974557224a59",
    )
    version(
        "0.7.4",
        sha256="be6407f4051d1db0134c3beeeb0bb71d3f9b9aceb953759c61c82b4689b6cd9e",
    )
    version(
        "0.7.5",
        sha256="5a0c6d38a6444fbe31d1724c14672181a264e48d755629b757e9b10c688685d9",
    )

    depends_on("py-maturin@1.0:2.0", type=("build"))
    depends_on("rust@1.87:", when="@0.8.0:", type=("build"))
    depends_on("rust@1.80:", when="@:0.7.5", type=("build"))
    depends_on("python@3.10:")
