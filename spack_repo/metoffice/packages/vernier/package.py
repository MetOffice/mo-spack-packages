# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

from spack.package import conflicts, depends_on, variant, version

from spack_repo.builtin.build_systems.cmake import CMakePackage


class Vernier(CMakePackage):
    """Vernier - profiler for scientific code on HPC platforms."""

    homepage = "https://github.com/MetOffice/Vernier"

    git = "https://github.com/MetOffice/Vernier.git"
    url = "https://github.com/MetOffice/Vernier/archive/refs/tags/0.3.0.tar.gz"
    # Head of trunk
    version("main", branch="main")
    
    version(
        "0.5.0",
        sha256="be1d2fbb16f30162d07fa80c7a2f03b4e85b07dda3898bff125fda3db8718477",
    )
    version(
        "0.4.1",
        sha256="7a677453a06e2c93aa9cb12af4b1a41de5434f98730f28259ad18bc571958276",
    )
    version(
        "0.4.0",
        sha256="12bfa7f759517dc566e88287490a423029937f4efdc18bc7a809d8edd37e8464",
    )
    version(
        "0.3.1",
        sha256="76567e028caff5df2e17c0f3cdd2f127794b3d16acf43c64b9d3b762503a6aa2",
    )
    version(
        "0.3.0",
        sha256="c549fd8ad09d2150e286e1ea25499bda5ecc19467020e505c2ec57c1141afc92",
    )

    variant("test", default=False, description="enable testing")
    variant(
        "max_label_length",
        default="256",
        values=("100", "256", "512"),
        when="@0.4.0:",
        description="maximum length of caliper labels",
    )

    depends_on("cmake@3.13:")
    depends_on("googletest@1.11.0:", when="+test")
    depends_on("pfunit+mpi", when="+test")
    depends_on("mpi")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    # See Vernier issue 212
    conflicts("^openmpi", when="@:0.4")

    def cmake_args(self):
        args = [
            self.define("ENABLE_DOXYGEN", False),
            self.define("ENABLE_SPHINX", False),
            self.define("INCLUDE_GTEST", False),
            self.define_from_variant("STRING_LENGTH", "max_label_length"),
            self.define_from_variant("BUILD_TESTS", "test"),
            self.define_from_variant("BUILD_FORTRAN_TESTS", "test"),
        ]

        return args

    def setup_run_environment(self, env):
        """Setup custom variables in the generated module file"""

        env.prepend_path("FFLAGS", "-I" + self.spec.prefix.include, " ")
        env.prepend_path("CPPFLAGS", "-I" + self.spec.prefix.include, " ")
        env.prepend_path(
            "LDFLAGS",
            "-L" + self.spec.prefix.lib64 + " -Wl,-rpath=" + self.spec.prefix.lib64,
            " ",
        )
