# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import AutotoolsPackage


class Yaxt(AutotoolsPackage):

    """Yaxt - Yet Another Exchange Tool."""

    homepage = "https://swprojects.dkrz.de/redmine/projects/yaxt"
    url = "https://gitlab.dkrz.de/dkrz-sw/yaxt/-/archive/v0.11.3/yaxt-v0.11.3.tar.gz"

    # Yaxt download locations are hard to determine systematically and
    # must be hardwired for each version
    version("0.11.3", sha256="32737a1c09156a1491c62fc3ec9e0eb8d1ef958c7e0a7042c7fba3b352d81cd8")
    version("0.11.2", sha256="e9a552641c3b52daed4d09a59ac879cbe7253acf8cb6d6855211f68c4d4f2227")
    version("0.11.1", sha256="29bfb8a773645efabecde4769b252573454b78ebf4c9041878ad9041d07bbb1b")
    version("0.11.0", sha256="1f0f9bb1f5a15f3c540034c4dc77298e9aebd1a286d810107b175d44e8216b2a")
    version("0.10.2", sha256="b4b7d19f4eed8d7e18a4d3b64089dc6f1c044d73205c8df7d6ea6b63ed1dc8e6")
    version("0.10.1", sha256="5282ec1b1afeb06c595fcf7cbd892f2c0e89b92da1a031e7bfdcb9b9ad8f2415")
    version("0.10.0", sha256="a7e104abf08d9119f8830ffbfefa61a8d631a1410940ad593bdae8ae76b7b669")
    version("0.9.3.1", sha256="53a95dd0c840a291478fc7aad40fd7eddd6c1637ed8ec0bfebeeb574066f83e9")
    version("0.9.3", sha256="43a3fab7cea7bc9e849afe9634902196ad850414aa10fcdb469f3c51900ed99a")
    version("0.9.2.1", sha256="d8b0333ea4c8965f4a11487ffbed7c02828b11f06d8d5e16e091941437596ddd")
    version("0.9.2", sha256="6c8bc440a63b0ee87947add65423d8b4c93ba453383f1e12c82befd0f8d461f5")
    version("0.9.1", sha256="10414d55a1e5572a5036d19830c499de5f6dfe9be4eb097b0009e27b81d6211b")
    version("0.9.0", sha256="8a403294ecc7a3d32e8b4f168f548b443f21dac7d846f7fe3b6242ca663fafb3")    

    depends_on("mpi")
    depends_on("autoconf", type="build", when=" build_system=autotools")
    depends_on("automake", type="build", when="build_system=autotools")
    depends_on("libtool", type="build", when="build_system=autotools")
    

    # Require generic-names when MPI is provided by intel-oneapi-mpi, e.g.
    # depends_on("intel-oneapi-mpi+generic-names")

    variant("idxlong", default=True, description="build with idxtype=long support")
    variant("notests", default=True, description="build without MPI tests")

    def patch(self):

        """Patch nvidia compiler problem.

        The nvidia compiler sets the __PGI preprocessor macro and
        reports a version > 22 but it does not support the parameter
        feature used by yaxt.  This forces the pre-22 behavior when
        building with the nvidia compiler by removing the version
        check from the conditional.
        """

        if "%nvhpc" in self.spec:
            filter_file(r"^(#if\s+(?:!\s+)?defined\s+__PGI)\s*\S+\s*__PGIC__.*",
                        r"\1",
                        "tests/ftest_common.f90",
                        backup=True)

        return

    def configure_args(self):

        """Add extra configuration flags."""

        env["CC"] = self.spec["mpi"].mpicc
        env["CXX"] = self.spec["mpi"].mpicxx
        env["F77"] = self.spec["mpi"].mpif77
        env["FC"] = self.spec["mpi"].mpifc

        extra_args = []

        if "+idxlong" in self.spec:
            extra_args.append("--with-idxtype=long")

        if "+notests" in self.spec:
            extra_args.append("--without-regard-for-quality")

        return extra_args
        
    def setup_run_environment(self, env):
        
        """Setup custom variables in the generated module file"""
        
        env.prepend_path("FFLAGS", "-I"+self.spec.prefix.include, " ")
        env.prepend_path("CPPFLAGS", "-I"+self.spec.prefix.include, " ")
        env.prepend_path("LDFLAGS", "-L" + self.spec.prefix.lib + " -Wl,-rpath=" + self.spec.prefix.lib, " ")
