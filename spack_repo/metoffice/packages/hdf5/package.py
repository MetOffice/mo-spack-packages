from spack_repo.builtin.packages.hdf5.package import Hdf5 as BaseHdf5
from spack.package import *


class Hdf5(BaseHdf5):

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
