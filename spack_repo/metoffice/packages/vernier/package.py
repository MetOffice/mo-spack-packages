# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Vernier(CMakePackage):
    """Vernier - profiler for scientific code on HPC platforms."""

    homepage = "https://github.com/MetOffice/Vernier"

    # At present, Vernier cannot currently be downloaded without a
    # user account that is part of the MetOffice organisation.  The
    # best solution is to manually download the tar file from github
    # to a local directory, cd to the directory, and add it to a
    # mirror with `spack mirror create -d <directory> -D vernier`
    git = "git@github.com:MetOffice/Vernier.git"
    url = "https://github.com/MetOffice/Vernier/archive/refs/tags/0.3.0.tar.gz"
    # Head of trunk
    version("develop")

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

    variant("gtest", default=False, description="enable testing")
    variant(
        "max_label_length",
        default="256",
        values=("100", "256", "512"),
        when="@0.4.0:",
        description="maximum length of caliper labels",
    )

    depends_on("cmake@3.13:")
    depends_on("googletest", when="+gtest")
    depends_on("pfunit", when="+gtest")
    depends_on("mpi")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    def cmake_args(self):
        args = [
            self.define("ENABLE_DOXYGEN", False),
            self.define("ENABLE_SPHINX", False),
            self.define("INCLUDE_GTEST", False),
            self.define_from_variant("STRING_LENGTH", "max_label_length"),
            self.define_from_variant("BUILD_TESTS", "gtest"),
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
