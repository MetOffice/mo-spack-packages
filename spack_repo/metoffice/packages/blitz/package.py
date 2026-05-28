# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------
from spack.package import depends_on, variant, ver, filter_file

import spack_repo.builtin.packages.blitz.package as BaseBlitz


class Blitz(BaseBlitz.Blitz):
    """N-dimensional arrays for C++"""

    variant("libpapi", default=False, description="Enable building blitz with PAPI counters")

    depends_on("papi@:5.7", type="link", when="+libpapi")

    def cmake_args(self):
        args = []
        if self.spec.satisfies("~libpapi"):
            args.extend([self.define("BZ_HAVE_LIBPAPI", "")])
        
        return args

    def patch(self):

        """Fix compiler vendor detection macros.

        Compiler vendor detection is broken on the Cray EX.  This adds
        a default to the m4 definition to target llvm when using a
        recent version of cce.
        """

        if "%cce" in self.spec and self.compiler.version >= ver(15):
            # Add a default compiler vendor and set it to llvm if
            # using a recent Cray compiler
            filter_file("^\)", "[COMPILER_VENDOR=\"llvm\"]\n)",
                        "m4/ac_compiler_specific_header.m4")
