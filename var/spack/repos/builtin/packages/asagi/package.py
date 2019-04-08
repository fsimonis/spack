# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
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
#     spack install asagi-git
#
# You can edit this file again by typing:
#
#     spack edit asagi-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Asagi(CMakePackage):
    """a pArallel Server for Adaptive GeoInformation."""

    homepage = "https://github.com/TUM-I5/ASAGI"
    git      = "https://github.com/TUM-I5/ASAGI.git"

    version('master', branch='master', submodules=True)

    variant('mpi', default=True)

    depends_on('mpi', when="+mpi")
    depends_on('netcdf +mpi', when="+mpi")
    depends_on('netcdf ~mpi', when="~mpi")
    depends_on('cmake')
    depends_on('python@2.7:')
