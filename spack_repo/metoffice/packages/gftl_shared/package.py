import os

import spack_repo.builtin.packages.gftl_shared.package as gftlShared
from spack.package import *


class GftlShared(gftlShared.GftlShared):

    def setup_run_environment(self, env):
        """Setup custom variables in the generated module file"""
        major_version, minor_version, _ = str(self.spec.version).split(".")
        prefix_subdir = os.path.join(
            self.spec.prefix,
            str(self.spec.name).upper().replace("-", "_")
            + "-"
            + major_version
            + "."
            + minor_version,
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
