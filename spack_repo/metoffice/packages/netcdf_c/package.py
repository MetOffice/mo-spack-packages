# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import spack_repo.builtin.packages.netcdf_c.package as netcdfCBase
from spack.package import *


class NetcdfC(netcdfCBase.NetcdfC):

    def setup_run_environment(self, env):
        """Setup custom variables in the generated module file"""

        env.prepend_path("CFLAGS", "-I" + self.spec.prefix.include, " ")
        env.prepend_path("FFLAGS", "-I" + self.spec.prefix.include, " ")
        env.prepend_path("CPPFLAGS", "-I" + self.spec.prefix.include, " ")
        env.prepend_path(
            "LDFLAGS",
            "-L" + self.spec.prefix.lib + " -Wl,-rpath=" + self.spec.prefix.lib,
            " ",
        )
