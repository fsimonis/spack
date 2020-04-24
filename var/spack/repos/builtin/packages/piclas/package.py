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
#     spack install piclas
#
# You can edit this file again by typing:
#
#     spack edit piclas
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Piclas(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/piclas-framework/piclas"
    git      = "https://github.com/piclas-framework/piclas.git"
    url      = "https://github.com/piclas-framework/piclas/archive/v1.6.0.tar.gz"
    # FIXME maintainers = ['github_user1', 'github_user2']

    version('develop', branch='master')
    version('1.6.0', sha256='8b27b24d73d5757c57d021d5b718dd19d8a04463152ad5787c0e4bbac05a72a9')

    depends_on('cmake@3.0:')
    depends_on('mpi')
    depends_on('netlib-lapack')
    depends_on('zlib')
    depends_on('hdf5+fortran+hl')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args

