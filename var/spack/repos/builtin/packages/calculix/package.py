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
#     spack install calculix
#
# You can edit this file again by typing:
#
#     spack edit calculix
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Calculix(CMakePackage):
    """A Free Software Three-Dimensional Structural Finite Element Program."""

    homepage = "http://www.calculix.de/"
    git      = "https://github.com/fsimonis/ccx.git"

    version('2.16', branch="cmake-port")

    depends_on('arpack-ng')
    depends_on('spooles@2.2:')
    depends_on('cmake@3.10:', type='build')
