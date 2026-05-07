# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

from spack_repo.builtin.packages.fargparse.package import Fargparse as BaseFargparse
import os


class Fargparse(BaseFargparse):
    def setup_run_environment(self, env):
        """Setup custom variables in the generated module file"""
        major_version, minor_version, _ = str(self.spec.version).split(".")
        prefix_subdir = os.path.join(
            self.spec.prefix,
            str(self.spec.name).upper() + "-" + major_version + "." + minor_version,
        )
        env.prepend_path("FFLAGS", "-I" + os.path.join(prefix_subdir, "include"), " ")
        env.prepend_path("CPPFLAGS", "-I" + os.path.join(prefix_subdir, "include"), " ")
        env.prepend_path(
            "LDFLAGS",
            "-L"
            + os.path.join(prefix_subdir, "lib")
            + " -Wl,-rpath="
            + os.path.join(prefix_subdir, "lib"),
            " ",
        )
