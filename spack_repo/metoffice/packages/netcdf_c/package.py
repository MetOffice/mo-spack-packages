# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

import spack_repo.builtin.packages.netcdf_c.package as netcdfCBase


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
