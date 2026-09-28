# -----------------------------------------------------------------------------
#  (C) Crown copyright Met Office. All rights reserved.
#  The file LICENCE, distributed with this code, contains details of the terms
#  under which the code may be used.
# -----------------------------------------------------------------------------

from spack.package import depends_on, license, version
from spack_repo.builtin.build_systems.python import PythonPackage


class PySphinxSitemap(PythonPackage):
    """A Sphinx extension to generate multiversion and multilanguage sitemaps.org
    compliant sitemaps for the HTML version of your Sphinx documentation
    """

    homepage = "https://github.com/jdillard/sphinx-sitemap"
    pypi = "sphinx-sitemap/sphinx_sitemap-2.6.0.tar.gz"
    license("MIT")

    version(
        "2.9.0",
        sha256="70f97bcdf444e3d68e118355cf82a1f54c4d3c03d651cd17fe87398b26e25e21",
    )
    version(
        "2.8.0",
        sha256="749d7184a0c7b73d486a232b54b5c1b38a0e2d6f18cf19fb1b033b8162b44a82",
    )
    version(
        "2.7.2",
        sha256="819e028e27579b47efa0e2f863b87136b711c45f13e84730610e80316f6883da",
    )
    version(
        "2.7.1",
        sha256="28f02df7062e83628e9782a0d9449658a79c9813217c51db086edc51f20e7bd5",
    )
    version(
        "2.7.0",
        sha256="0b2f8440b95b10e6a944968594655ba5d1bf279f700e226f64bdf30edded50f9",
    )
    version(
        "2.6.0",
        sha256="5e0c66b9f2e371ede80c659866a9eaad337d46ab02802f9c7e5f7bc5893c28d2",
    )

    depends_on("python@3.8:", when="@2.6.0")
    depends_on("py-setuptools", type="build")
    depends_on("py-six")
    depends_on("py-sphinx@1.2:", when="@2.6.0")
