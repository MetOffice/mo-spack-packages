# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *
from spack.llnl.util.filesystem import install_tree


class PyRosePicker(PythonPackage):
    """py-rose-picker - metadata utility for LFRIC."""

    homepage = "https://github.com/MetOffice/rose_picker"
    url = "https://github.com/MetOffice/rose_picker"
    git = "git@github.com:MetOffice/rose_picker.git"

    version("develop", branch="main")
    depends_on("python@3:")
    depends_on("py-setuptools", type="build")
