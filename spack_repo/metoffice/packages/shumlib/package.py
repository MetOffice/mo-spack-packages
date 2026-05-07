# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import depends_on, variant, version


class Shumlib(CMakePackage):
    """Shared UM Library.

    Shumlib is the collective name for a set of libraries which are
    used by the UM; the UK Met Office's Unified Model, that may be of
    use to external tools or applications where identical
    functionality is desired. The hope of the project is to enable
    developers to quickly and easily access parts of the UM code that
    are commonly duplicated elsewhere, at the same time benefiting
    from any improvements or optimisations that might be made in
    support of the UM itself.
    """

    homepage = "https://github.com/MetOffice/shumlib"
    url = "https://github.com/MetOffice/shumlib/archive/refs/tags/2025.10.1.tar.gz"
    git = "https://github.com/MetOffice/shumlib.git"

    version("main", branch="main")

    # FIXME: placeholder pointing to existing makefile version
    version(
        "2025.10.1",
        sha256="9947c4bc53f6177ec98d751bf296d55e429a7c66fae73178645bed849029bc0f",
    )

    depends_on("cmake@3.13:", type="build")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    variant("ieee", default=False, description="use Fortran intrinsic IEEE features")
    variant("nan", default=False, description="check NaNs by bitwise inspection")
    variant(
        "denormal", default=False, description="check denormals by bitwise inspection"
    )

    variant("openmp", default=True, description="enable OpenMP support")
    variant("fthreads", default=False, description="enable Fortran OpenMP everywhere")
    variant("test", default=False, description="enable testing")

    def cmake_args(self):
        """Set CMake build arguments."""

        args = [
            self.define_from_variant("IEEE_ARITHMETIC", "ieee"),
            self.define_from_variant("NAN_BY_BITS", "nan"),
            self.define_from_variant("DENORMAL_BY_BITS", "denormal"),
            self.define_from_variant("BUILD_OPENMP", "openmp"),
            self.define_from_variant("BUILD_FTHREADS", "fthreads"),
            self.define_from_variant("BUILD_TESTS", "test"),
        ]

        return args

    def setup_run_environment(self, env):
        """Setup custom variables in the generated module file"""

        env.prepend_path("FFLAGS", "-I" + self.spec.prefix.include, " ")
        env.prepend_path("CPPFLAGS", "-I" + self.spec.prefix.include, " ")
        env.prepend_path(
            "LDFLAGS",
            "-L" + self.spec.prefix.lib + " -Wl,-rpath=" + self.spec.prefix.lib,
            " ",
        )
