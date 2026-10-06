# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

import json
import os
from spack.llnl.util.tty import warn
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Gcom(CMakePackage):

    homepage = "https://github.com/MetOffice/gcom"
    git = "git@github.com:MetOffice/gcom.git"

    version("main", branch="main")

    variant("parallel", default=True, description="build with MPI")
    variant("openmp", default=False, description="build with OpenMP")

    variant("shared", default=False, description="build shared library")
    variant("with32", default=True, description="build with 32 bit precision")
    variant("tests", default=True, description="build test commands")

    variant(
        "buffer_size",
        default="160000",
        values=("160000", "1920000", "4000000", "15000000"),
        description="MPI communication buffer size",
    )

    depends_on("mpi", when="+parallel")

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    # Required until gcom source code is relocated
    build_directory = "mybuild"

    def cmake_args(self):

        if self.spec.satisfies("%gcc"):
            preset_name = "debug-gcc"
        else:
            raise ValueError("unsupported compiler")

        args = [
            "--preset",
            preset_name,
            self.define_from_variant("ENABLE_MPI", "parallel"),
            self.define_from_variant("ENABLE_OPENMP", "openmp"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("BUILD_TESTS", "tests"),
            self.define_from_variant("BUFFER_SIZE", "buffer_size"),
        ]

        return args
