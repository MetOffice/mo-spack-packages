# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

from spack_repo.builtin.packages.py_fparser.package import PyFparser as PyFparserBase
from spack.package import version

class PyFparser(PyFparserBase):
    """Extension of the central Spack fparser package"""
    
    version(
        "0.2.2", 
        sha256="81fee12416cde2dc57782542e4e271a1155e6f7a16eab099c030d54ff1b56b8c"
    )
    version(
        "0.2.1", 
        sha256="1ca89a760ef23747fc54c53918c03d9165026736d9f0ea6347885bd79fe4be85"
    )

    
    
