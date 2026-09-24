# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

import os
import textwrap

from spack.package import (
    Executable,
    InstallError,
    Package,
    depends_on,
    env,
    filter_file,
    install_tree,
    join_path,
    mkdirp,
    run_after,
    touch,
    variant,
    version,
)
from spack_repo.builtin.packages.boost.package import Boost


class Xios(Package):
    """XIOS package. XML-IO-SERVER library for IO management of climate models."""

    url = "https://gitlab.in2p3.fr/ipsl/projets/xios-projects/xios/-/archive/xios-3.0.1.0/xios-xios-3.0.1.0.tar.gz"
    git = "https://gitlab.in2p3.fr/ipsl/projets/xios-projects/xios.git"

    # XIOS 3
    version("3.0.4.0", tag="xios-3.0.4.0")
    version(
        "3.0.1.0",
        sha256="d357e81d9139eb0e7cc15664297851042340ca57a8e84a92b0d0847b8a7c8bfb",
    )

    # XIOS 2
    version(
        "2.2701", commit="2eb572f0986eca19031eb6c294d116646010687c"
    )  # equivalent sha to legacy svn revision 2701

    variant("oasis", default=False, description="enable OASIS support")
    variant(
        "mode",
        values=("debug", "dev", "prod"),
        default="prod",
        description="Build for debugging, development or production",
    )
    depends_on("netcdf-c+mpi", type=("build", "link"))
    depends_on("netcdf-fortran", type=("build", "link"))
    depends_on("hdf5+mpi", type=("build", "link"))
    depends_on("mpi")
    depends_on("curl")

    # TODO: replace this with an explicit list of components of Boost,
    # for instance depends_on('boost +filesystem')
    # See https://github.com/spack/spack/pull/22303 for reference
    depends_on(Boost.with_default_variants)
    depends_on("blitz")
    depends_on("perl", type="build")
    depends_on("perl-uri", type="build")
    depends_on("gmake", type="build")

    depends_on("boost")
    depends_on("oasis", type=("build", "link", "run"), when="+oasis")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    def xios_fcm(self):
        """Create an fcm configuration for the current system.

        Override the method in the base package to create a modified
        fcm configuration for the latest releases of XIOS.  Fixes
        include the addition of the -lstdc++ flag and a flag to
        support long source lines in gfortran.
        """

        file = join_path("arch", "arch-SPACK.fcm")
        spec = self.spec
        param = {}
        param["MPICXX"] = spec["mpi"].mpicxx
        param["MPIFC"] = spec["mpi"].mpifc
        param["CC"] = self.compiler.cc
        param["FC"] = self.compiler.fc
        param["BOOST_INC_DIR"] = spec["boost"].prefix.include
        param["BOOST_LIB_DIR"] = spec["boost"].prefix.lib
        param["BLITZ_INC_DIR"] = spec["blitz"].prefix.include
        param["BLITZ_LIB_DIR"] = spec["blitz"].prefix.lib
        if spec.satisfies("%apple-clang"):
            param["LIBCXX"] = "-lc++"
        else:
            param["LIBCXX"] = "-lstdc++"

        if spec.satisfies("%gcc"):
            # Allow long lines in gfortran
            param["FFLAGS"] = "-ffree-line-length-none"
        else:
            param["FFLAGS"] = ""

        # Note: removed "%intel", "%apple-clang", "%clang", "%fj" from
        # the list on the assumption that the flags will need changing
        # to work with these compilers
        if any(
            map(spec.satisfies, ("%gcc", "%cce", "%intel", "%oneapi"))
        ) and self.spec.satisfies("@=2.2701"):
            text = textwrap.dedent(
                """
            %CCOMPILER      {MPICXX}
            %FCOMPILER      {MPIFC}
            %LINKER         {MPIFC}

            %BASE_CFLAGS    -ansi -w -D_GLIBCXX_USE_CXX11_ABI=0 \
            -I{BOOST_INC_DIR} -std=c++11
            %PROD_CFLAGS    -O3 -DBOOST_DISABLE_ASSERTS
            %DEV_CFLAGS     -g -O2
            %DEBUG_CFLAGS   -g

            %BASE_FFLAGS    -D__NONE__ {FFLAGS}
            %PROD_FFLAGS    -O3
            %DEV_FFLAGS     -g -O2
            %DEBUG_FFLAGS   -g

            %BASE_INC       -D__NONE__
            %BASE_LD        -L{BOOST_LIB_DIR} -L{BLITZ_LIB_DIR} -lblitz {LIBCXX}

            %CPP            {CC} -E
            %FPP            {CC} -E -P -x c
            %MAKE           gmake
            """
            ).format(**param)
        elif spec.satisfies("%gcc"):
            text = textwrap.dedent(
                """
            %CCOMPILER      {MPICXX}
            %FCOMPILER      {MPIFC}
            %LINKER         {MPIFC}

            %BASE_CFLAGS    -w -std=c++11 -D__XIOS_EXCEPTION
            %PROD_CFLAGS    -O3 -DBOOST_DISABLE_ASSERTS
            %DEV_CFLAGS     -g -O2
            %DEBUG_CFLAGS   -g

            %BASE_FFLAGS    -D__NONE__ {FFLAGS}
            %PROD_FFLAGS    -O3
            %DEV_FFLAGS     -g -O2
            %DEBUG_FFLAGS   -g

            %BASE_INC       -D__NONE__
            %BASE_LD        {LIBCXX}

            %CPP            {CC} -E
            %FPP            {CC} -E -P -x c
            %MAKE           gmake
            """
            ).format(**param)
        elif spec.satisfies("%cce"):
            text = textwrap.dedent(
                """
            %CCOMPILER      {MPICXX}
            %FCOMPILER      {MPIFC}
            %LINKER         {MPIFC}

            %BASE_CFLAGS    -std=c++11 -DMPICH_SKIP_MPICXX
            %PROD_CFLAGS    -O3 -DBOOST_DISABLE_ASSERTS
            %DEV_CFLAGS     -O2
            %DEBUG_CFLAGS   -g

            %BASE_FFLAGS    -em -m 4 -e0 -eZ  {FFLAGS}
            %PROD_FFLAGS    -O1
            %DEV_FFLAGS     -G2
            %DEBUG_FFLAGS   -g

            %BASE_INC       -D__NONE__
            %BASE_LD        -D__NONE__ {LIBCXX}

            %CPP            {CC} -E
            %FPP            {CC} -E -P -x c
            %MAKE           gmake

            bld::tool::fc_modsearch -J
            """
            ).format(**param)
        else:
            raise InstallError("Unsupported compiler.")

        with open(file, "w") as f:
            f.write(text)

    def install(self, spec, prefix):
        """Replacement install method."""

        env["CC"] = spec["mpi"].mpicc
        env["CXX"] = spec["mpi"].mpicxx
        env["F77"] = spec["mpi"].mpif77
        env["FC"] = spec["mpi"].mpifc

        options = [
            "--full",
            f"--{spec.variants['mode'].value}",
            "--arch",
            "SPACK",
            "--netcdf_lib",
            "netcdf4_par",
            "--job",
            str(make_jobs),  # noqa: F821
        ]

        if "+oasis" in self.spec:
            # Add OASIS build flag
            options += ["--use_oasis", "oasis3_mct"]

            # Save OASIS flags for later use
            self.oasis_incdir = join_path(self.spec["oasis"].prefix, "include")
            self.oasis_libdir = join_path(self.spec["oasis"].prefix, "lib")
            self.oasis_lflags = "-lpsmile.MPI1 -lscrip -lmct -lmpeu"

        else:
            self.oasis_incdir = None
            self.oasis_libdir = None
            self.oasis_lflags = None

        self.xios_env()
        self.xios_path()
        self.xios_fcm()

        make_xios = Executable("./make_xios")
        make_xios(*options)

        mkdirp(spec.prefix)
        install_tree("bin", spec.prefix.bin)
        install_tree("lib", spec.prefix.lib)
        install_tree("inc", spec.prefix.include)
        install_tree("etc", spec.prefix.etc)
        install_tree("cfg", spec.prefix.cfg)

    def xios_env(self):
        """Create XIOS environment file.

        The parent method creates an empty file.  Overload this to add
        OASIS environment variables if necessary.
        """

        # This creates an empty environment file
        file = join_path("arch", "arch-SPACK.env")
        touch(file)

        if "-oasis" in self.spec:
            # Do nothing if OASIS is not enabled
            return

        # Add OASIS compiler settings to the env file
        with open(join_path("arch", "arch-SPACK.env"), "w") as f:
            print(f'export OASIS_INCDIR="-I{self.oasis_incdir}"', file=f)
            print(f'export OASIS_LIBDIR="-L{self.oasis_libdir}"', file=f)
            print(f'export OASIS_LIB="{self.oasis_lflags}"', file=f)

    def xios_path(self):
        file = join_path("arch", "arch-SPACK.path")
        spec = self.spec
        paths = {
            "NETCDF_INC_DIR": spec["netcdf-c"].prefix.include,
            "NETCDF_LIB_DIR": spec["netcdf-c"].prefix.lib,
            "NETCDFF_INC_DIR": spec["netcdf-fortran"].prefix.include,
            "NETCDFF_LIB_DIR": spec["netcdf-fortran"].prefix.lib,
            "HDF5_INC_DIR": spec["hdf5"].prefix.include,
            "HDF5_LIB_DIR": spec["hdf5"].prefix.lib,
            "BOOST_INC_DIR": spec["boost"].prefix.include,
            "BOOST_LIB_DIR": spec["boost"].prefix.lib,
        }
        text = textwrap.dedent(
            """
        NETCDF_INCDIR="-I{NETCDF_INC_DIR} -I{NETCDFF_INC_DIR}"
        NETCDF_LIBDIR="-L{NETCDF_LIB_DIR} -L{NETCDFF_LIB_DIR}"
        NETCDF_LIB="-lnetcdff -lnetcdf"

        MPI_INCDIR=""
        MPI_LIBDIR=""
        MPI_LIB="-lcurl"

        HDF5_INCDIR="-I {HDF5_INC_DIR}"
        HDF5_LIBDIR="-L {HDF5_LIB_DIR}"
        HDF5_LIB="-lhdf5_hl -lhdf5"

        BOOST_INCDIR="-I {BOOST_INC_DIR}"
        BOOST_LIBDIR=""
        BOOST_LIB=""

        OASIS_INCDIR=""
        OASIS_LIBDIR=""
        OASIS_LIB=""
        """
        )
        with open(file, "w") as f:
            f.write(text.format(**paths))

        if "-oasis" in self.spec:
            # Do nothing if OASIS is not enabled
            return

        def replacer(match):
            """Add the correct OASIS flags"""
            if match.group(1).endswith("INCDIR"):
                setting = f"-I{self.oasis_incdir}"
            elif match.group(1).endswith("LIBDIR"):
                setting = f"-L{self.oasis_libdir}"
            elif match.group(1).endswith("LIB"):
                setting = self.oasis_lflags
            return f'{match.group(1)}="{setting}"'

        # Use spack's filter_file with a custom replacement function
        # to change all the OASIS flags in a single operation
        filter_file(
            r"^\s*(OASIS_[^=]+)=.*",
            replacer,
            join_path("arch", "arch-SPACK.path"),
            backup=True,
        )

    @run_after("install")
    def remove_fcm_env(self):
        """Remove broken fcm_env.ksh symlink."""
        target = os.path.join(self.spec.prefix.bin, "fcm_env.ksh")
        if os.path.islink(target):
            os.unlink(target)

    def setup_run_environment(self, env):
        """Setup custom variables in the generated module file"""

        env.prepend_path("FFLAGS", "-I" + self.spec.prefix.include, " ")
        env.prepend_path("CPPFLAGS", "-I" + self.spec.prefix.include, " ")
        env.prepend_path(
            "LDFLAGS",
            "-L" + self.spec.prefix.lib + " -Wl,-rpath=" + self.spec.prefix.lib,
            " ",
        )
        env.set("XIOS_VERSION", str(self.spec.version))
