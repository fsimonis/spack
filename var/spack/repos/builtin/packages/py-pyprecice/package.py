# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-pyprecice
#
# You can edit this file again by typing:
#
#     spack edit py-pyprecice
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyPyprecice(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.precice.org"
    url = "https://pypi.io/packages/source/p/pyprecice/pyprecice-2.0.0.1.tar.gz"
    git = "https://github.com/precice/python-bindings"
    maintainers = ['BenjaminRueth']

    import_modules = ['precice']

    version('develop', branch='develop')
    version('2.0.2.1', sha256='180bf9d57b9d19b546033ad7d796d8ca187257e3ef391d5fb5fc4ed510bcdbad')
    version('2.0.1.1', sha256='816783c11b2bb23784c19486b725d8a3bef822b906ed23e40caa98e9c3535951')
    version('2.0.0.1', sha256='2102c1c258fc769754239ec0682a3ab5ea1092b63b81c876fcef6646f4c6cf3f')

    #extends('python')

    depends_on('python@3:', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-wheel', type='build')
    depends_on('py-pip', type='build')
    depends_on('py-cython', type='build')
    depends_on('py-packaging', type='build')
    depends_on('py-mpi4py', type='run')

    # preCICE per-version dependencies
    depends_on('precice@develop', when='@develop')
    for v in ['2.0.2', '2.0.1', '2.0.0']:
        depends_on('precice@'+v, when='@{v}.0:{v}.99'.format(v=v))

    # patch('remove_pip_check.patch')

    def url_for_version(self, version):
        url = "https://pypi.io/packages/source/p/pyprecice/pyprecice-{}.tar.gz"
        return url.format(version)
